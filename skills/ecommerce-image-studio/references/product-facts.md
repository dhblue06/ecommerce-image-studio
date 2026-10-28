# 每款商品的事实档案

所有图型共享事实源，不能每张图重新猜商品。档案用于制作，不是规格认证。模板：../assets/product-facts.template.json。

## 保存与复用

在用户目录或当前批次下的 `products/<商品标识>/<颜色或变体>/product-facts.json` 保存；SKU未知用临时标识，写`sku:null`，不编造真实SKU。每款/颜色一份；同系列可共享已证实结构，但不能自动继承功率、尺寸、容量、配件或颜色。建立档案所需内容从现有素材提取，单张白底仅填写身份必要项，其余留空，不为补齐模板强迫客户填表。

新任务若用户明确指定旧档案，或同项目已有同款匹配来源，先核对sku、variant、source摘要/文件哈希和修订版本，再复用。没有源文件访问能力可记录引用或手动来源，不能编造哈希。新图型号/结构/接口不同则暂停冲突字段，先做无关图或询问一次。不能仅因文件名/颜色相近合并。

## 字段与证据

- identity：商品形状、颜色、品牌和标识位置、实际可见结构、接口/按键/线缆、禁改细节。每个字段引用evidence_ids，不能只有无来源自由文本。
- facts：单独的容量/功率/尺寸/兼容/材质/装箱数量等；fact_id稳定，value、unit、conditions、evidence_ids及status分开。
- evidence：source_id/文件或用户消息引用/区域定位、观察原文、source_kind及sha256（可读取时）。区域可用文字位置，无精确框就不伪造坐标。
- source_kind：photo_observation、packaging_text、user_spec、document、measurement。来源与状态不混为一谈。
- status：visible（实物可见）、supplied（用户提供）、packaging_claim（包装标称）、measured（有实际测量记录）、unknown、conflict。状态不代表工具已认证。
- sale_contents：实际售卖数量与included_items/not_included_items，分别引用证据；包装图片里出现的手机、道具不自动算配件。
- conflicts/unknowns：记录争议、影响的字段和待确认问题；不选择数值更大或更好卖的一边。
- identity_lock：仅由有依据identity/facts导出，短而具体；未知材质不写“铝合金”，不可见结构不补细节。
- change_log：revision、改动fact_ids、旧值摘要、原因与新证据；不覆盖历史证据。

纯生成结果只能作为output_reference，不可升级为photo_observation/真实规格证据。包装图含原有认证印刷可忠实保留，但不等于可以另画一个认证徽章或宣称已核验资质。

## 与套图关联

shot-plan通过`product_record.path/record_id/revision`绑定档案；claims引用fact_ids，shots引用claim_ids和直接fact_ids。claim仅把事实转为有条件的利益，不新增性能推断。claim的source/status继承档案，不维护一份相互矛盾的规格副本。出图时保存实际使用的identity/style lock快照，便于追踪。

修订事实后检查哪些claim和slot依赖该fact，标`needs_review`；只有确实受影响的图需要重做。与改动无关的合格图复用。若颜色/形状等身份锁变化，则该变体所有产品图都应复核；不得只修文案却保留错款实物。

## 简短操作例

包装写10000mAh：fact=10000，unit=mAh，status=packaging_claim，引用包装文字位置；文案可按标称信息处理，不推断给手机充几次。用户后来确认另一型号20000mAh时，不把旧SKU直接改容量；先确认是否为新变体。
