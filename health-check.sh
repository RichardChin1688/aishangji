#!/bin/bash
echo "=== 1. 飞书配置 ==="
cat ~/.openclaw/feishu/config.json

echo ""
echo "=== 2. 主配置中的飞书插件 ==="
cat ~/.openclaw/openclaw.json | grep -B2 -A10 feishu || echo "未在 openclaw.json 中找到 feishu 配置"

echo ""
echo "=== 3. 网关状态 ==="
openclaw gateway status 2>&1

echo ""
echo "=== 4. 日志错误 ==="
echo "--- commands.log 最近错误 ---"
tail -50 ~/.openclaw/logs/commands.log | grep -i "error\|fail" || echo "无报错"

echo ""
echo "--- config-audit.jsonl 最近记录 ---"
tail -10 ~/.openclaw/logs/config-audit.jsonl

echo ""
echo "=== 5. 飞书凭证 ==="
echo "--- feishu-pairing.json ---"
cat ~/.openclaw/credentials/feishu-pairing.json
echo ""
echo "--- feishu-default-allowFrom.json ---"
cat ~/.openclaw/credentials/feishu-default-allowFrom.json

echo ""
echo "=== 6. 进程检查 ==="
ps aux | grep -i openclaw | grep -v grep

echo ""
echo "=== 7. 磁盘空间 ==="
df -h ~
