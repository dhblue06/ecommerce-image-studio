# 电商图片平台规则

核验日期：2026-10-27。官方来源优先于本地默认；这些资料并非所有站点/品类的完整政策。独立站没有全球统一的白底、占比或图片张数要求。再次核验时只读所需平台，保留日期、生效日期和访问限制。

欧洲新增渠道、图片位置及可访问性记录见 [europe-channels.md](europe-channels.md)；Facebook/Instagram目录不能与Feed混用，Google Business不能与Shopping混用。制作profile中的尺寸/比例/占比可为本地默认，不全部是官方硬要求。

## Google Merchant Center

来源：
- https://support.google.com/merchants/answer/6324350?hl=en
- https://support.google.com/merchants/answer/18353357?hl=en

实际商品与所选变体一致，清楚展示销售内容；不加入非同售物品、宣传叠字、水印、边框或占位图。主图与附图的用途分开。保留商品自身真实印刷，不把禁止新增悬浮标识理解成应擦掉商品商标。

官方最佳实践：完整轮廓占画面 75%–90%，清晰对焦；推荐白色或浅中性纯色背景，也接受符合规则的场景图，不把白底说成所有品类的硬要求。推荐 1500×1500 或以上。规则页公告所有产品至少 500×500 将于 2027-01-31 生效；页面表格已显示该数值，不能忽略生效日期反推所有现行旧规格。本 skill 直接以 2048 方图为推荐输出目标，实际尺寸另核。

文件限制：不超过 64MP、16MB；支持 JPEG、WebP、PNG 等列明格式。包装图片应展示立体盒体，非仅平面正面。AI 生成图片须有 AI 来源元数据，保留 IPTC DigitalSourceType 等已有标签；不要把写一句提示词当作文件标记已完成。缺失时标 metadata pending。

提交层面图片 URL 需可访问、格式与扩展名相符，但此 skill 不负责网站部署或 feed 同步。若用户要求上线合规，除文件检查外还需后续流程验证可抓取性及落地页一致性。

## Amazon MAIN 与附图

公开官方资料：
- https://sell.amazon.com/blog/product-photos （当前可读；85% 或以上、尺寸/格式、拍摄指引）
- https://sellercentral.amazon.com/seller-forums/discussions/t/04805fc7-b165-472c-9339-725d1c2b52dc （Amazon 员工指引；更新于约三年前，非最新完整分类政策）
- https://sellercentral.amazon.com/help/hub/reference/external/G1881?itemid=200164650 （详细要求；本次打开为登录/JS页，未完整读取）
- https://sellercentral.amazon.com/gp/help/external/GNRP6DDJV79DUHRD （详细帮助；本次打开为登录/JS页，未完整读取）

通用基线：MAIN 为准确、专业的商品图，纯白背景 RGB 255,255,255，主体至少占画面约 85%，完整展示，不因填画面裁掉零件。无新增文字、logo、水印、边框或背景图形；不擦掉商品自身真实商标。只展示销售款式及包含的配件，不把正背多视角拼成多个实物。通常将商品从包装取出，包装只有属于重要产品特征等适用例外时才可出现在 MAIN；否则作包装附图。服饰模特、珠宝、食品等按具体站点品类指南处理。

公开摄影页列最长边 500–10000 像素，支持 JPEG/TIFF/PNG/非动画 GIF；JPEG 优先见员工指引。不要将“1000px 支持缩放”的常见帮助口径混作全部场景最低上传值；正式提交需核对当前站点。此 skill 推荐母版2048方图，并核查真实分辨率，不宣称2048是Amazon强制尺寸。

本地执行：MAIN 目标最长边占比约 88%、参考范围85%–90%，不是官方上限；不得以Google允许75%为理由放行Amazon的79%主图。参考不足的包装插图重建不自动视为真实实物照片或合规MAIN；需实物核对、必要时补拍。不要推断Amazon一律禁止或一律允许AI编辑，关键是准确性及当前平台/品类政策；本次未取得完整登录后政策，标明限制。

附图可按适用规则展示场景、细节、包装或信息说明；不是可以随意添加虚假认证、评价、排名、促销信息。图像位置、站点及品类有差异，不将MAIN的纯白/完整占比规则套到所有附图。

## 独立站：Shopify / PrestaShop / WooCommerce

官方来源：
- https://help.shopify.com/en/manual/products/product-media/product-media-types
- https://woocommerce.com/document/adding-product-images-and-galleries/

Shopify：当前产品/系列图上限5000×5000或25MP、文件小于20MB；方形2048×2048通常显示最佳；主图比例一致利于系列列表排列。支持PNG/JPEG/WebP等，实际展示与主题有关。这些是Shopify限制，不代表PrestaShop或所有独立站。

WooCommerce：推荐至少800×800，细节多时更高；主题和图库组件决定显示宽度、裁切及缩放，后台可生成各显示尺寸。800不是统一上限，也不是跨平台推荐母版尺寸。

本地默认：目录白底图1:1、2048目标、最长边约85%，统一色彩、视觉比例和光影。不是独立站官方统一硬要求。场景和细节图可以不同构图，但按实际页面预期导出，检查移动端可读性和安全裁切。有主题信息时兼顾显示尺寸与清晰度，按支持格式导出压缩副本；不靠一个固定KB值牺牲细节。平台/主题未知就标默认方案，不虚构PrestaShop统一限额。

PrestaShop按实际版本、主题image types和服务器上传限制处理；详见europe-channels.md新增PrestaShop条目与官方来源。`prestashop-pdp`仅为本地白底母版预检配置，不是所有店铺上传规范。

独立站同步Google Shopping时，另满足Google feed图片规则；站内允许的宣传图不等于可直接用作Google或Amazon主图。不要为平台推荐的多张图片数量自动扩大用户交付范围。
