"""Read-only image preflight. Pillow required. No threshold segmentation or fixes.

Coordinates follow EXIF-transposed display; bbox is x0,y0,x1,y1 (exclusive end).
Reviewed mask: L image, 255=known background, 0=ignore. No mask completeness claim.
Exit 0=selected checks had no failure, 1=check failed, 2=invalid input.
Always leaves platform readiness pending visual/policy review, even on exit 0.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

PROFILE_PATH = Path(__file__).resolve().parents[1] / 'references' / 'export-profiles.json'


def profiles():
    return json.loads(PROFILE_PATH.read_text(encoding='utf-8'))['profiles']


def analyse(path, profile, bbox=None, bbox_reviewed=False, background_mask=None,
            mask_reviewed=False):
    path = Path(path)
    cfg = profiles()[profile]
    checks, issues = {}, []

    def check(name, ok, actual, expected):
        checks[name] = {'status': 'pass' if ok else 'fail', 'actual': actual,
                        'expected': expected}

    with Image.open(path) as raw:
        fmt, frames = raw.format, getattr(raw, 'n_frames', 1)
        info_keys = sorted(str(k) for k in raw.info)
        im = ImageOps.exif_transpose(raw).convert('RGBA')
    w, h = im.size
    size = path.stat().st_size
    check('static', frames == 1, frames, 1)
    if 'formats' in cfg:
        check('format', fmt in cfg['formats'], fmt, cfg['formats'])
    for key, actual in [('min_width', w), ('min_height', h), ('min_long', max(w,h))]:
        if key in cfg:
            check(key, actual >= cfg[key], actual, cfg[key])
    for key, actual in [('max_long', max(w,h)), ('max_pixels', w*h)]:
        if key in cfg:
            check(key, actual <= cfg[key], actual, cfg[key])
    if 'max_mb' in cfg:
        check('file_size_max', size < cfg['max_mb'] * 1000000, size,
              {'less_than_bytes': cfg['max_mb'] * 1000000})
    if 'min_kb' in cfg:
        check('file_size_min', size >= cfg['min_kb'] * 1000, size,
              {'at_least_bytes': cfg['min_kb'] * 1000})
    ratio = cfg.get('ratio')
    if ratio:
        check('production_ratio', abs(w/h - ratio[0]/ratio[1]) < 0.002,
              [w,h], {'local_default': ratio})
    if cfg.get('opaque'):
        alpha_min = im.getchannel('A').getextrema()[0]
        check('opaque', alpha_min == 255, alpha_min, 255)
    if cfg.get('transparent'):
        alpha_range = im.getchannel('A').getextrema()
        check('has_transparent_background_and_opaque_subject',
              alpha_range[0] == 0 and alpha_range[1] == 255,
              list(alpha_range), [0,255])
        issues.append('Alpha extrema only: review subject preservation, holes and edge halos on light/dark previews.')
    if min(w,h) < cfg.get('recommended_short', 0):
        issues.append('Below recommended production resolution; not a minimum-policy verdict.')
    framing = {'status': 'unknown', 'method': None, 'ratio': None}
    if bbox is not None:
        x0,y0,x1,y1 = bbox
        if not (0 <= x0 < x1 <= w and 0 <= y0 < y1 <= h):
            raise ValueError('bbox outside EXIF-transposed image or empty')
        framing = {'status': 'reviewed' if bbox_reviewed else 'unreviewed',
                   'method': 'user-supplied-bbox', 'bbox_exclusive': list(bbox),
                   'ratio': max((x1-x0)/w,(y1-y0)/h)}
        if bbox_reviewed:
            check('edge_margin', x0 > 0 and y0 > 0 and x1 < w and y1 < h,
                  list(bbox), 'no subject edge touches canvas')
            if 'coverage' in cfg:
                lo,hi = cfg['coverage']
                check('local_framing_range', lo <= framing['ratio'] <= hi,
                      framing['ratio'], [lo,hi])
        else:
            issues.append('bbox not reviewed: coverage not accepted as a check.')
    elif 'coverage' in cfg:
        issues.append('No reviewed subject bbox; framing unknown. Do not infer from nonwhite pixels.')
    background = {'status': 'unknown', 'method': None}
    if background_mask:
        with Image.open(background_mask) as raw_mask:
            mask = ImageOps.exif_transpose(raw_mask).convert('L')
        if mask.size != im.size:
            raise ValueError('background mask dimensions differ from EXIF-transposed image')
        binary = mask.point(lambda v: 255 if v >= 128 else 0)
        count = binary.histogram()[255]
        if count == 0:
            raise ValueError('background mask contains no selected pixels')
        rgb = im.convert('RGB')
        selected = [rgb.getchannel(c).histogram(binary) for c in ('R','G','B')]
        # Per-channel non-white counts are informational only; do pixel conjunction below.
        exact = 0
        for pixel, chosen in zip(im.getdata(), binary.getdata()):
            if chosen and pixel == (255,255,255,255):
                exact += 1
        background = {'status': 'reviewed-region' if mask_reviewed else 'unreviewed',
                      'method': 'supplied-background-mask', 'selected_pixels': count,
                      'exact_white_ratio': exact/count,
                      'channel_ranges': [[next(i for i,n in enumerate(hist) if n),
                                          max(i for i,n in enumerate(hist) if n)]
                                         for hist in selected],
                      'mask_completeness': 'not_verified'}
        if mask_reviewed and cfg.get('white'):
            check('selected_background_exact_white', exact == count, exact/count, 1.0)
        if not mask_reviewed:
            issues.append('background mask not reviewed: not used to pass background check.')
    elif cfg.get('white'):
        issues.append('Pixel-white background unknown: no reviewed background mask.')
    if cfg.get('ai_metadata'):
        issues.append('AI origin metadata semantics and preservation require separate review.')
    issues.append('Identity, included items, claims, text, crop integrity and current country policy require review.')
    fail = any(c['status'] == 'fail' for c in checks.values())
    return {'file': str(path.resolve()), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'profile': profile, 'dimensions': [w,h], 'format': fmt, 'bytes': size,
            'checks_pass': not fail, 'checks': checks, 'framing': framing,
            'background': background, 'metadata_keys_present': info_keys,
            'policy_review': cfg.get('policy_review'), 'platform_ready': False,
            'status': 'needs_fix' if fail else 'pending_visual_and_policy_review',
            'issues': issues, 'mutated_image': False}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('image', nargs='?')
    ap.add_argument('--profile', choices=list(profiles()), default='shopify-pdp')
    ap.add_argument('--list-profiles', action='store_true')
    ap.add_argument('--bbox', help='x0,y0,x1,y1 exclusive, display orientation')
    ap.add_argument('--bbox-reviewed', action='store_true')
    ap.add_argument('--background-mask')
    ap.add_argument('--mask-reviewed', action='store_true')
    ap.add_argument('--out')
    args = ap.parse_args()
    if args.list_profiles:
        print(json.dumps(profiles(), ensure_ascii=False, indent=2))
        return 0
    if not args.image:
        ap.error('image is required unless --list-profiles')
    try:
        bbox = tuple(map(int,args.bbox.split(','))) if args.bbox else None
        if bbox is not None and len(bbox) != 4:
            raise ValueError('bbox needs four integers')
        if args.out and Path(args.out).resolve() == Path(args.image).resolve():
            raise ValueError('report must not overwrite input image')
        if args.out and args.background_mask and Path(args.out).resolve() == Path(args.background_mask).resolve():
            raise ValueError('report must not overwrite mask')
        if args.out and Path(args.out).exists():
            raise ValueError('report exists; choose a new filename')
        r = analyse(args.image, args.profile, bbox, args.bbox_reviewed,
                    args.background_mask,args.mask_reviewed)
        rendered = json.dumps(r,ensure_ascii=False,indent=2)
        if args.out:
            Path(args.out).write_text(rendered,encoding='utf-8')
        print(rendered)
        return 0 if r['checks_pass'] else 1
    except (ValueError, OSError, KeyError) as exc:
        print(json.dumps({'error': str(exc)},ensure_ascii=False),file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
