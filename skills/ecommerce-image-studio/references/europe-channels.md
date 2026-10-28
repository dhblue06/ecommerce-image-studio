# 欧洲渠道与图片位置

核验 2026-10-27。平台位置优先于平台名称；下列尺寸若标“本地建议”不代表官方最低值。不能从页面域名的 `seller-es` 推断内容适用西班牙，必须读 Applies to。基础 Google Shopping、Amazon、Shopify 规则见 platform-rules.md。

| 渠道/位置 | 制作默认 | 内容与验收重点 | 证据范围 |
|---|---|---|---|
| Amazon MAIN | 2048方图；本地占比88% | 白底、真实款式和销售数量，通常不含包装，无新增叠字 | 通用公开指引；ES/DE/FR/IT等类别正式提交前核对 |
| Amazon 附图 / A+ | 附图2048方图；A+按选定模块 | 附图说明、尺寸、场景可用；A+与商品图库不是同一规格 | A+模块尺寸不在此硬编码，取得所选模块及桌面/移动规格后制作 |
| Shopify 商品页 | 2048方图母版 | 背景可按品牌，主图比例统一，留可缩放细节，轻量导出版 | 官方当前限额见 platform-rules.md；同步Shopping另验Google规则 |
| PrestaShop 商品封面/图库/变体图 | 本地默认2048方图母版、最长边约85% | 封面、包装、细节分开；颜色变体准确；按实际主题 image types 比例适配，避免二次留白或裁切 | PrestaShop没有统一2048或85%硬要求；上传大小及格式依版本、服务器与模块核对 |
| Google Shopping | 2048方图；本地占比85% | 无营销叠字，变体正确，AI来源元数据 | 官方75%–90%为构图建议 |
| Google Business Profile 商品/商家照片 | 720方图导出版 | 真实照片、克制编辑，勿虚构环境；不要求Shopping式85% | 官方JPG/PNG、10KB–5MB、推荐720×720、最小250×250 |
| Facebook/Instagram 商品目录 | 本地建议2048方图、JPEG、<8MB | 清洁商品图，与社交广告分开；若渠道限制不同以当前目录规范为准 | Meta官方页本次登录/限流，数值为保守制作目标，不认证平台限额 |
| Facebook/Instagram Feed 帖子或创意 | 本地建议1080×1350或1080方图 | 有依据的短文案、场景、移动可读；轮播比例一致 | 官方访问受限，非宣称只支持这两种比例；广告须核对具体版位 |
| Instagram/Facebook Story、Reels静态封面 | 本地建议1080×1920 | 9:16独立布局、产品/文案避UI、检查封面中心裁切 | 生产模板，不等于视频/完整广告；安全区随版位复查 |
| TikTok Shop 商品图 | 本地建议2048方图 | 实物准确、正面主图、配件真实、无额外促销标记；保留实拍依据 | UK旧指南与西语站资料可读，不能外推为全EU规则；参考800方图口径，当前国家再核对 |
| TikTok 社交图片/封面 | 本地建议1080×1920 | 情境清晰、短句、中央安全区，不仿造TikTok界面/平台认证 | 不套Shop商品图规则；不以封面代替视频 |
| TikTok Standard Carousel 广告 | 官方列1200×628、640×640、720×1280 | 2–35张，JPG/PNG，≤100KB为建议；音乐与投放配置由其他流程负责 | 2026-09官方资源页；不是TikTok Shop或全部图片广告统一规则 |
| Pinterest 普通/标准广告 Pin | 1000×1500，2:3 | 商品使用灵感、少量可读文字，长图可能被裁 | 官方推荐；PNG/JPEG，桌面20MB/app32MB；平台会对近白背景加显示层 |
| Pinterest retail catalog 商品 Pin | 母版或导出≥1000×1500，优先2:3 | 商品一致，图像URL能抓取，禁占位图；保留无营销字版 | 本次官方image_link字段明确至少1000×1500，别把附图75×75最低值当主图标准 |
| Miravia 主图/附图 | 本地建议2048方图、JPEG、<5MB | 主图白底、真实款式、无额外营销字；包装默认附图 | Miravia举办培训明确强调白底；Seller Center详细尺寸未完整读取，本地数值非认证限额 |
| AliExpress EU 主图/变体/附图 | 本地建议2048方图、JPEG、<5MB | 清洁完整真实产品，变体单独；包插图重建仅作待核对稿 | EU完整规范未读取；CIS官方资料仅区域参考，不移植为EU硬规则 |

## 官方来源与访问限制

- PrestaShop图片类型/母版：https://docs.prestashop-project.org/v.8-documentation/user-guide/improving-shop/customizing-store-design/image-settings 。平台由母版生成不同缩略图，主题可定义自己的图片尺寸；该页为v8文档，不把Classic默认值当全部版本标准。https://help-center.prestashop.com/hc/en-us/articles/18502655219602--Optimize-the-images 建议按实际显示尺寸优化文件，WebP用于已确认支持的环境，JPEG/PNG兼容导出。不把客户“定制商品上传图”的64px等配置误当商家商品图限制。

PrestaShop制作约定：无主题配置时先做2048方图母版，声明为本地默认，不查询网站或修改主题。已有image types/尺寸时优先适配实际cover/large/home/cart等用途，名称与数值以该店为准；不自动生成全部缩略图、不触发缩略图重建。默认产品封面优先，包装作单独图库附图；变体图各自绑定真实款式。上传版优先JPEG，保留PNG母版；WebP只在版本/模块支持确认后另导出。需要Google Shopping时复用清洁母版并叠加其元数据等检查。可在交付记录提供建议排序和变体归属，不实际上传、设封面或同步库存。

- Google Business：https://support.google.com/business/answer/6103862?hl=es ，清晰、真实、不过度编辑的照片要求；https://support.google.com/business/answer/7213077?hl=en ，内容政策。
- Meta目录规范（由Shopify官方链接确认目标）：https://www.facebook.com/business/help/686259348512056?id=725943027795860 。Meta目录字段：https://developers.facebook.com/docs/marketing-api/catalog/reference/ 。本次登录/429，未完整核验条目；不从第三方指南补成“官方已确认”。
- Meta广告：https://www.facebook.com/business/ads-guide/image/facebook-feed 、https://www.facebook.com/business/ads-guide/image/instagram-feed ；Instagram照片：https://help.instagram.com/1631821640426723 。本次均登录或429；正式投放前在对应Ads Manager版位再验。
- TikTok Shop：https://seller-es.tiktok.com/university/essay?knowledge_id=7753820806006530&lang=es ，列至少800×800、最多9张方图和真实商品要求；页面地区须现场再读。https://seller-es.tiktok.com/university/essay?knowledge_id=6130104607426336&lang=en-GB ，标UK、2024-11-21，明确不能全部是数字呈现。另一个knowledge_id=7073362639816491虽位于seller-es域名却标US，本skill不采用其600px为EU统一标准。
- TikTok轮播：https://ads.tiktok.com/resources/help/article/specifications-for-carousel-ads?lang=en 。
- Pinterest规格：https://help.pinterest.com/en/business/article/pinterest-product-specs ；目录：https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs 。
- Miravia官方举办培训：https://app.livestorm.co/miravia/mejores-practicas-para-los-titulos-e-imagenes-de-tus-productos ；https://seller.miravia.es/ 本次未能读取详细后台规范。培训说明不是完整SKU/品类上传标准。
- AliExpress EU规则入口：https://rulechannel.aliexpress.com/ 本次不可读取。区域参考：https://business.aliexpress-cis.com/help/article/images-requirements （CIS：5MB、JPEG/PNG、白/浅色背景、商品≥70%等，且主图不得用渲染；不作为EU已核验政策）。

## 欧洲本地化与来源标记

国家、语言、货币及单位属于独立字段，英国不等于EU，西班牙不等于西语所有市场。保留原包装语言；社交附加文案默认es-ES只在用户没指定时使用，不能把包装上的英语自动翻成错误规格。用户要求翻译包装属于再设计任务，应另确认目标，不混进白底抠图。

不生成虚假CE、能效等级、EU产地、消费者评价或功效对照。没有规格就不做精确尺寸图。AI来源标记/平台披露不靠抹水印解决，保留已有IPTC/C2PA等来源信息；具体披露要求在相应渠道复核，不能宣称同一AI标签适用所有欧洲平台。
