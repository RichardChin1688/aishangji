#!/bin/bash
echo "=== 检查 OpenClaw 配置 ==="
cat ~/.openclaw/agents/main/config.json 2>/dev/null | grep -i feishu || echo "无飞书配置"
cat ~/.openclaw/agents/main/config.json 2>/dev/null | grep -i sandbox || echo "无 sandbox 配置"

echo ""
echo "=== 检查飞书环境变量 ==="
env | grep -i feishu || echo "无飞书环境变量"

echo ""
echo "=== 检查网关状态 ==="
openclaw gateway status 2>/dev/null || echo "网关命令不可用"

echo ""
echo "=== 检查网关日志 ==="
ls -la ~/.openclaw/gateway/logs/ 2>/dev/null || echo "日志目录不存在"
tail -50 ~/.openclaw/gateway/logs/*.log 2>/dev/null | grep -i feishu || echo "无飞书相关日志"
