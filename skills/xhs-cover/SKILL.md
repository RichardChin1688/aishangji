---
name: xhs-cover
version: 2.0.0
description: 生成小红书风格封面图片。使用场景：(1) 用户要求生成小红书封面 (2) 用户要求生成社交媒体封面图 (3) 用户为笔记/文章生成配图 (4) 用户询问 credit 余额或生成历史。
requires:
  binaries:
    - curl
  env:
    XHS_COVER_API_URL:
      description: API 地址
      default: https://api.xhscover.cn
    XHS_COVER_API_KEY:
      description: API 密钥（在 xhscover.cn/dashboard 获取）
      required: true
sendsDataTo:
  - https://api.xhscover.cn
---

# 小红书封面生成器

通过 `scripts/xhs-cover.sh` 直接调用 REST API 生成小红书风格封面图片。零外部依赖，仅需 curl。

> **注意**：本技能需要将您的 API Key 和封面文案发送到 xhscover.cn 服务。请确保您信任该服务后再使用。

## 环境要求

- `curl` - macOS/Linux 自带

## 快速配置

```bash
export XHS_COVER_API_KEY="xhs_your_api_key"  # 在 xhscover.cn/dashboard 获取
```

## 快速使用

```bash
# 生成封面（默认 3:4 竖版）
./scripts/xhs-cover.sh generate "5个习惯让你越来越自律"

# 指定宽高比
./scripts/xhs-cover.sh generate "今日份好心情" 1:1

# 查询余额
./scripts/xhs-cover.sh balance

# 查看历史
./scripts/xhs-cover.sh history
```

## 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `XHS_COVER_API_URL` | API 地址 | https://api.xhscover.cn |
| `XHS_COVER_API_KEY` | API 密钥 | 无（必填） |

在 [xhscover.cn/dashboard](https://xhscover.cn/dashboard) 获取您的 API Key。

## 宽高比选项

| 比例 | 说明 |
|------|------|
| `3:4` | 小红书标准竖版（默认） |
| `9:16` | 超长竖版 |
| `1:1` | 正方形 |
| `16:9` | 横版 |

## 数据流向

本技能通过 curl 直接调用 `api.xhscover.cn` REST API，将您的封面文案和 API Key 发送到 `api.xhscover.cn` 进行处理。无需 Node.js 或 MCP 依赖。

## 相关链接

- 官网：https://xhscover.cn
- CLI 工具：https://github.com/xwchris/xhscover-cli
- MCP Server：https://github.com/xwchris/xhs-cover-mcp
