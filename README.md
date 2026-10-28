# 电商图片工作室

根据产品照片和有据卖点生成欧洲电商图片的独立 Skill。只做图片、图内文案与验收，不写 listing 或同步网站。

## 使用

将本仓库目录保存为 ecommerce-image-studio，放入支持 Skill 的工具的 skills 目录。入口为 [SKILL.md](SKILL.md)。需要可用的图片生成或编辑工具。

上传参考图后选择：

1. 产品白底图
2. 包装白底图
3. 卖点电商套图
4. 产品白底与包装白底，各一张独立文件
5. 产品透明背景 PNG

例如：`4，PrestaShop` 或 `3，Amazon，西语`。保留完整线缆、挂卡等，白底主体最长边目标约 85%；平台差异见 references。商品事实和重建限制必须核对，不能保证平台审核通过。

## 目录

- SKILL.md：入口
- agents/：技能元数据
- references/：平台规则、图型、品类、事实与验收
- assets/：事实与套图计划模板
- scripts/：只读图片预检及测试
- ecommerce-image-studio.zip：打包下载版本

## 预检

Python 环境安装 Pillow 后运行：

```shell
python scripts/preflight.py image.png --profile prestashop-pdp --out report.json
python -m unittest discover -s scripts -p "test_*.py"
```

预检不能替代人工比对产品、文字、背景孔洞和平台政策。平台资料来源及核验限制见 references。
