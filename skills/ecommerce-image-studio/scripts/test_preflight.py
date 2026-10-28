"""Focused regressions for read-only preflight; synthetic fixtures only."""
import hashlib
import tempfile
import unittest
from pathlib import Path
from PIL import Image, ImageDraw
from preflight import analyse, profiles


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)
        self.path = self.folder/'product.png'
        im = Image.new('RGB',(1000,1000),'white')
        ImageDraw.Draw(im).rectangle((60,200,939,799), fill='black')
        im.save(self.path)

    def tearDown(self):
        self.temp.cleanup()

    def test_all_profiles_parse(self):
        self.assertEqual(len(profiles()),17)

    def test_transparent_product_rejects_white_background(self):
        r=analyse(self.path,'transparent-product')
        self.assertEqual(r['checks']['has_transparent_background_and_opaque_subject']['status'],'fail')

    def test_transparent_product_accepts_real_alpha(self):
        im=Image.new('RGBA',(1000,1000),(0,0,0,0))
        ImageDraw.Draw(im).rectangle((60,200,939,799),fill=(255,255,255,255))
        im.save(self.path)
        r=analyse(self.path,'transparent-product')
        self.assertEqual(r['checks']['has_transparent_background_and_opaque_subject']['status'],'pass')

    def test_empty_transparent_image_rejected(self):
        Image.new('RGBA',(1000,1000),(0,0,0,0)).save(self.path)
        r=analyse(self.path,'transparent-product')
        self.assertEqual(r['checks']['has_transparent_background_and_opaque_subject']['status'],'fail')

    def test_no_bbox_unknown_and_no_compliance_pass(self):
        r = analyse(self.path,'amazon-main')
        self.assertEqual(r['framing']['status'],'unknown')
        self.assertFalse(r['platform_ready'])

    def test_reviewed_88_percent(self):
        r = analyse(self.path,'amazon-main',(60,200,940,800),True)
        self.assertTrue(r['checks']['local_framing_range']['status']=='pass')

    def test_google_79_not_amazon(self):
        box = (100,200,890,800)
        self.assertEqual(analyse(self.path,'google-shopping',box,True)['checks']['local_framing_range']['status'],'pass')
        self.assertEqual(analyse(self.path,'amazon-main',box,True)['checks']['local_framing_range']['status'],'fail')

    def test_unreviewed_box_not_pass(self):
        r = analyse(self.path,'amazon-main',(60,200,940,800))
        self.assertNotIn('local_framing_range',r['checks'])

    def test_white_product_not_inferred(self):
        Image.new('RGB',(1000,1000),'white').save(self.path)
        self.assertEqual(analyse(self.path,'amazon-main')['framing']['status'],'unknown')

    def test_reviewed_white_and_residue_mask(self):
        mask = Image.new('L',(1000,1000),255)
        ImageDraw.Draw(mask).rectangle((60,200,939,799),fill=0)
        mp = self.folder/'mask.png'
        mask.save(mp)
        r = analyse(self.path,'amazon-main',background_mask=mp,mask_reviewed=True)
        self.assertEqual(r['checks']['selected_background_exact_white']['status'],'pass')
        im = Image.open(self.path).convert('RGB')
        im.putpixel((10,10),(254,254,254)); im.save(self.path)
        r = analyse(self.path,'amazon-main',background_mask=mp,mask_reviewed=True)
        self.assertEqual(r['checks']['selected_background_exact_white']['status'],'fail')

    def test_transparency(self):
        Image.new('RGBA',(1000,1000),(255,255,255,0)).save(self.path)
        self.assertEqual(analyse(self.path,'amazon-main')['checks']['opaque']['status'],'fail')

    def test_invalid_bbox_and_mask(self):
        with self.assertRaises(ValueError):
            analyse(self.path,'amazon-main',(-1,0,500,500),True)
        mp=self.folder/'small.png'; Image.new('L',(2,2),255).save(mp)
        with self.assertRaises(ValueError):
            analyse(self.path,'amazon-main',background_mask=mp)

    def test_pinterest_catalog_and_pin_different(self):
        self.assertNotIn('min_height',analyse(self.path,'pinterest-pin')['checks'])
        self.assertEqual(analyse(self.path,'pinterest-catalog')['checks']['min_height']['status'],'fail')

    def test_no_mutation(self):
        before=hashlib.sha256(self.path.read_bytes()).hexdigest()
        analyse(self.path,'amazon-main',(60,200,940,800),True)
        self.assertEqual(before,hashlib.sha256(self.path.read_bytes()).hexdigest())


if __name__ == '__main__':
    unittest.main()
