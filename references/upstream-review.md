# 上游研究与取舍

研究日期2026-10-27；https://github.com/xianyu110/ecommerce-image-skills ，重点阅读README、amazon-white-background/SKILL.md、ecommerce-listing-suite/SKILL.md及其check_main_image.py。该项目已包含Amazon，并非仅国内平台。

借鉴设计原则：商品身份锁、图型规划、清洁母版与创意图分离、批次风格一致、结构化输出及断点续作。我们独立实现欧洲渠道表、制作profile与只读预检；未复制其生成器/检查脚本，也不引入其第三方接口推荐、商业链接或固定模型别名。

上游检查脚本将“距白色大于阈值”的像素当主体，框外当背景；修复会漂白近白像素并裁切/补边。白色商品、透明部分、阴影和线缆孔洞下存在误判风险，因此本skill不沿用自动通过或自动漂白逻辑。主体框/mask需人工确认；没有可靠证据则unknown。预检通过不代表平台合规。

上游许可证为MIT，Copyright (c) 2026 xianyu110：https://github.com/xianyu110/ecommerce-image-skills/blob/main/LICENSE 。未来若复制其代码或实质内容，须保留版权与完整MIT许可；目前为结构思路参考与独立实现。
