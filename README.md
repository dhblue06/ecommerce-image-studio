# 电商图片工作室 · 可安装插件

包含白底图、透明PNG与有据卖点套图工作流，适配欧洲电商渠道。插件版本：1.0.0。

## 从 GitHub 安装

在支持插件 marketplace 的 Codex CLI 中添加本仓库：

```shell
codex plugin marketplace add dhblue06/ecommerce-image-studio
```

若 `codex plugin` 不被识别，说明当前CLI不支持该命令；请使用支持插件功能的客户端版本，不要反复运行旧CLI。

然后在 ChatGPT 桌面应用的 Plugins 中选择“电商图片工作室”来源，安装 ecommerce-image-studio；必要时重启应用，再开启新对话使用。添加 marketplace 与完成插件安装是两个步骤。

支持工作区导入的管理员也可在 Admin > Plugins > Add > Import marketplace 中填写：

- Source: https://github.com/dhblue06/ecommerce-image-studio
- Path: 留空
- Branch: main

导入与可用性受账号、客户端和工作区策略控制。本仓库尚未提交或获批公共插件目录；普通聊天粘贴链接不保证完成安装。不要将它配置为自定义 MCP 服务器，本插件没有服务器地址。

官方规范：https://developers.openai.com/plugins/build/plugins
工作区导入：https://learn.chatgpt.com/docs/enterprise/plugin-management

## 使用

上传参考图并选择：

1. 产品白底图
2. 包装白底图
3. 卖点电商套图
4. 产品白底1张＋包装白底1张，两个独立文件
5. 产品透明背景PNG

例如：`4，PrestaShop` 或 `3，Amazon，西语`。不同款式分开处理；完整包含线缆、表带、挂卡等；常规白底最长边目标约85%，Amazon另按主图规则处理。

需要宿主提供图片生成/编辑工具。插件不附带图像模型、API密钥、外部MCP、自动执行hook或网站同步能力。文件预检需要Python与Pillow，不能替代产品保真与平台政策的人工核验。

## 项目结构

```text
plugin.json                         # 可移植插件清单
.codex-plugin/plugin.json           # Codex兼容清单
.agents/plugins/marketplace.json    # 仓库安装来源
skills/ecommerce-image-studio/      # 插件实际加载的完整Skill
  SKILL.md
  agents/
  assets/
  references/
  scripts/
SKILL.md, agents/, assets/, references/, scripts/ # 保留的独立Skill旧入口
ecommerce-image-studio.zip         # 独立Skill下载包
```

插件加载 skills/ecommerce-image-studio/；根目录旧Skill保持兼容，不作为插件第二份加载入口。更新工作流时应同步这两份内容并提高插件版本。

## 检查

```shell
python -m unittest discover -s skills/ecommerce-image-studio/scripts -p "test_*.py"
python skills/ecommerce-image-studio/scripts/preflight.py image.png --profile prestashop-pdp --out report.json
```

清单结构、源码一致性检查与实际客户端安装是不同验证；未在目标账号完成安装之前不能声称已可在该账号调用。
