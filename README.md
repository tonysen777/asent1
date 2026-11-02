# AsenT1 — Free AI Director Skill Gateway

AsenT1 是一个面向 AI 视频制作者的免费导演工作流入口。公开仓库只提供轻量客户端 Skill、连接说明和工具协议；**不包含 AsenT1 私有核心规则、内部参考资料、提示词模板库或研究归档**。

## 当前状态

- Public gateway: `asent1`
- Core runtime: separate private repository / hosted service
- Remote MCP endpoint: **尚未部署**
- 免费使用：目标产品政策；实际开放前会公布额度与服务状态

> 重要：目前仓库提供的是接入入口，不代表远程服务已经上线。未配置有效 MCP endpoint 时，Skill 必须明确报告“服务尚未连接”，不得假装调用成功。

## Claude Managed Agents 接入

1. 将本仓库作为 GitHub repository resource 挂载到 Managed Agents Session，以发现 `.claude/skills/asent1-video-production/SKILL.md`。
2. 在 Agent 配置中注册 AsenT1 远程 MCP server。
3. 在 Session 的 Vault 中配置服务端要求的认证信息。
4. 新建 Session 后，Agent 才会读取该次挂载的仓库版本。

MCP endpoint 尚未发布，示例配置见 [`docs/managed-agents.md`](docs/managed-agents.md)。

## 设计边界

- SSS1 是独立项目，AsenT1 不替代、不合并 SSS1。
- AsenT1 的历史来源是原 KSR 项目；历史仓库保留，不作为公开运行入口。
- 本仓库不提供私有核心文件的下载入口。
- 用户只通过远程 MCP 工具使用服务；核心规则由服务端管理。

## 远程工具

工具契约见 [`docs/mcp-tools.md`](docs/mcp-tools.md)。服务端部署完成前，工具调用不可用。

## 反馈

欢迎提交文档问题、安装问题和不含内部规则的使用反馈。不要提交第三方课程、付费 Skill 原文、私人剧本、API Key 或任何未经授权的材料。
