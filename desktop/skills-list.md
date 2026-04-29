# OpenClaw 免费技能清单

> 📋 共收录 53 个官方技能，以下精选 15 个免费实用技能，优先推荐业务相关（电商/教育/数据分析）

---

## 🛒 电商/业务类

### 1. ordercli 🛵
**功能：** Foodora 外卖订单管理 CLI
- 查看历史订单和活跃订单状态
- 订单跟踪、重新下单
- 支持 Foodora（Deliveroo 开发中）
- **安装：** `brew install steipete/tap/ordercli` 或 `go install`

### 2. blogwatcher 📰
**功能：** 博客/RSS/Atom 订阅监控
- 监控多个博客和 RSS 源更新
- 自动扫描新文章、标记已读
- 适合竞品监控、行业资讯追踪
- **安装：** `go install github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest`

### 3. trello 📋
**功能：** Trello 项目管理
- 管理看板、列表、卡片
- 创建/移动卡片、添加评论
- 适合电商项目任务追踪
- **安装：** 需 `jq` + Trello API Key/Token

---

## 📊 数据分析/办公类

### 4. nano-pdf 📄
**功能：** PDF 自然语言编辑
- 用自然语言指令修改 PDF 内容
- 支持指定页面编辑
- 适合报表、文档快速修改
- **安装：** `uv install nano-pdf`

### 5. summarize 🧾
**功能：** URL/视频/文件智能摘要
- 一键摘要网页文章、YouTube 视频
- 支持播客转录、长文提取
- 适合竞品分析、行业报告速读
- **安装：** `brew install steipete/tap/summarize`

### 6. oracle 🧿
**功能：** 代码库智能问答
- 打包代码文件 + 提示词，向 AI 提问
- 支持浏览器模式（GPT-5.2 Pro）和 API 模式
- 适合代码审查、技术调研
- **安装：** `npm install -g @steipete/oracle`

### 7. gh-issues 🐛
**功能：** GitHub Issue 自动修复
- 自动抓取 Issue、派生子 Agent 修复、开 PR
- 支持并行处理、PR 评论自动回复
- 适合开源项目维护、自动化 Bug 修复
- **安装：** 需 `curl` + `git` + `gh` CLI + GitHub Token

---

## 💻 开发/协作类

### 8. coding-agent 🧩
**功能：** 代码开发 Agent 调度
- 调度 Codex/Claude Code/Pi 等编码 Agent
- 支持后台运行、PR 审查、批量修复
- 适合大型代码重构、功能开发
- **安装：** `npm install -g @anthropic-ai/claude-code` 或 `@openai/codex`

### 9. github 🐙
**功能：** GitHub 全功能 CLI
- Issue/PR 管理、CI 状态查看
- 代码审查、API 查询
- 适合日常 GitHub 工作流
- **安装：** `brew install gh` 或 `apt install gh`

### 10. discord 🎮
**功能：** Discord 机器人操作
- 发送消息、反应、创建投票
- 频道管理、线程创建
- 适合社区运营、通知推送
- **安装：** 需配置 Discord Token

### 11. slack 💬
**功能：** Slack 工作区管理
- 消息发送/编辑/删除
- 反应、置顶、成员查询
- 适合团队协作自动化
- **安装：** 需配置 Slack Bot Token

### 12. notion 📝
**功能：** Notion API 集成
- 创建/管理页面、数据库
- 数据查询、块内容编辑
- 适合知识库、CRM 数据管理
- **安装：** 需 Notion API Key

---

## 🎓 教育/学习类

### 13. gemini ✨
**功能：** Google Gemini CLI
- 一键问答、摘要、内容生成
- 支持 JSON 输出、多模型选择
- 适合快速学习、研究辅助
- **安装：** `brew install gemini-cli`

### 14. openai-whisper 🎤
**功能：** 本地语音转文字
- 离线转录音频文件
- 支持多语言、字幕生成
- 适合课程转录、会议记录
- **安装：** `brew install openai-whisper`

### 15. taskflow 🪝
**功能：** 多步骤任务流管理
- 跨会话任务编排、状态持久化
- 支持等待外部事件、子任务链接
- 适合复杂业务流程自动化
- **安装：** 内置技能，无需安装

---

## 📌 快速安装指南

```bash
# 1. 查看已安装技能
ls ~/.npm-global/lib/node_modules/openclaw/skills/

# 2. 安装技能依赖（示例）
brew install gh summarize ordercli gemini-cli openai-whisper
npm install -g @steipete/oracle @anthropic-ai/claude-code
go install github.com/Hyaxia/blogwatcher/cmd/blogwatcher@latest
uv install nano-pdf

# 3. 配置 API Key（如需要）
# Notion: ~/.config/notion/api_key
# GitHub: gh auth login
# Trello: export TRELLO_API_KEY / TRELLO_TOKEN
```

---

## 🔍 完整技能列表（53 个）

```
1password, apple-notes, apple-reminders, bear-notes, blogwatcher, blucli, 
bluebubbles, camsnap, canvas, clawhub, coding-agent, discord, eightctl, 
gemini, gh-issues, gifgrep, github, gog, goplaces, healthcheck, himalaya, 
imsg, mcporter, model-usage, nano-pdf, node-connect, notion, obsidian, 
openai-whisper, openai-whisper-api, openhue, oracle, ordercli, peekaboo, 
sag, session-logs, sherpa-onnx-tts, skill-creator, slack, songsee, 
sonoscli, spotify-player, summarize, taskflow, taskflow-inbox-triage, 
things-mac, tmux, trello, video-frames, voice-call, wacli, weather, xurl
```

---

> 💡 **提示：** 以上技能均为免费开源技能，部分需要配置 API Key 或 OAuth Token。安装前请阅读对应技能的 `SKILL.md` 了解详细配置步骤。
