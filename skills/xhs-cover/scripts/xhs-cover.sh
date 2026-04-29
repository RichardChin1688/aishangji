#!/bin/bash
# xhs-cover.sh - 小红书封面生成 CLI
# 零依赖，仅需 curl（macOS/Linux 自带）

set -e

# 默认配置
API_URL="${XHS_COVER_API_URL:-https://api.xhscover.cn}"
API_KEY="${XHS_COVER_API_KEY:-}"

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

error() { echo -e "${RED}错误: $1${NC}" >&2; exit 1; }
success() { echo -e "${GREEN}$1${NC}"; }
info() { echo -e "$1"; }

# 从 JSON 字符串中提取值（纯 grep/sed，不依赖 jq）
json_str() {
  echo "$1" | grep -o "\"$2\":\"[^\"]*\"" | head -1 | sed 's/.*:"//;s/"$//'
}

json_num() {
  echo "$1" | grep -o "\"$2\":[0-9]*" | head -1 | sed 's/.*://'
}

# API 请求
api_call() {
  local method="$1"
  local path="$2"
  local body="$3"

  local args=(-s -X "$method" \
    -H "Content-Type: application/json" \
    -H "X-API-Key: $API_KEY")

  if [ -n "$body" ]; then
    args+=(-d "$body")
  fi

  local resp
  resp=$(curl "${args[@]}" "${API_URL}${path}" 2>&1) || error "请求失败，请检查网络连接"

  # 检查 API 错误
  local err_msg
  err_msg=$(json_str "$resp" "error")
  if [ -n "$err_msg" ]; then
    error "$err_msg"
  fi

  echo "$resp"
}

check_config() {
  if [ -z "$API_KEY" ]; then
    error "请设置 XHS_COVER_API_KEY 环境变量\n  export XHS_COVER_API_KEY=\"xhs_your_api_key\"\n  在 https://xhscover.cn/dashboard 获取"
  fi
}

# 生成封面
generate_cover() {
  local text="$1"
  local ratio="${2:-3:4}"

  if [ -z "$text" ]; then
    error "请提供封面文案\n  用法: $0 generate <文案> [宽高比]"
  fi

  check_config

  info "生成封面: ${YELLOW}${text}${NC}"
  info "宽高比: ${ratio}"
  info "提交中..."

  # 提交生成任务
  local resp
  resp=$(api_call POST "/api/v1/generate" "{\"text\":\"$text\",\"aspectRatio\":\"$ratio\"}")

  local task_id
  task_id=$(json_str "$resp" "taskId")
  if [ -z "$task_id" ]; then
    error "创建任务失败，未返回 taskId"
  fi

  # 轮询等待结果
  local elapsed=0
  local interval=2
  local timeout=60

  while [ "$elapsed" -lt "$timeout" ]; do
    sleep "$interval"
    elapsed=$((elapsed + interval))

    resp=$(api_call GET "/api/v1/generate/${task_id}")
    local status
    status=$(json_str "$resp" "status")

    case "$status" in
      completed)
        local result_url credit_cost
        result_url=$(json_str "$resp" "resultUrl")
        credit_cost=$(json_num "$resp" "creditCost")
        echo ""
        success "封面生成完成！"
        info "图片地址: ${CYAN}${result_url}${NC}"
        [ -n "$credit_cost" ] && info "消耗积分: ${credit_cost}"
        return 0
        ;;
      failed)
        local err
        err=$(json_str "$resp" "errorMessage")
        error "生成失败: ${err:-未知错误}"
        ;;
      *)
        info "等待中... (${elapsed}s)"
        ;;
    esac
  done

  error "生成超时（${timeout}s），任务 ID: ${task_id}"
}

# 查询余额
get_balance() {
  check_config

  local resp
  resp=$(api_call GET "/api/v1/credits")

  local balance purchased used
  balance=$(json_num "$resp" "balance")
  purchased=$(json_num "$resp" "totalPurchased")
  used=$(json_num "$resp" "totalUsed")

  success "积分余额"
  echo "   当前余额: ${balance}"
  echo "   已购买:   ${purchased}"
  echo "   已使用:   ${used}"
}

# 获取历史
get_history() {
  local limit="${1:-10}"

  check_config

  info "获取最近 ${limit} 条记录..."

  local resp
  resp=$(api_call GET "/api/v1/user/history?page=1&limit=${limit}")

  local total
  total=$(json_num "$resp" "total")
  echo ""
  info "共 ${total} 条记录，显示最近 ${limit} 条："
  echo ""

  # 解析 tasks 数组中的每个条目
  echo "$resp" | grep -o '"id":"[^"]*"' | sed 's/"id":"//;s/"$//' | while read -r id; do
    local prompt status_line
    prompt=$(echo "$resp" | grep -o "\"${id}[^\}]*" | grep -o '"prompt":"[^"]*"' | head -1 | sed 's/"prompt":"//;s/"$//')
    status_line=$(echo "$resp" | grep -o "\"${id}[^\}]*" | grep -o '"status":"[^"]*"' | head -1 | sed 's/"status":"//;s/"$//')
    echo "  - [${status_line}] ${prompt}"
  done

  local count
  count=$(echo "$resp" | grep -o '"id":"[^"]*"' | wc -l | tr -d ' ')
  if [ "$count" -eq 0 ]; then
    info "   暂无记录"
  fi
}

# 显示帮助
show_help() {
  cat << EOF
小红书封面生成器 v2.0.0

用法:
  $0 generate <文案> [宽高比]   生成封面（含轮询等待）
  $0 balance                    查询积分余额
  $0 history [数量]             获取生成历史
  $0 help                       显示帮助

环境变量:
  XHS_COVER_API_URL   API 地址 (默认: https://api.xhscover.cn)
  XHS_COVER_API_KEY   API 密钥（必填，在 xhscover.cn/dashboard 获取）

宽高比:
  3:4   小红书标准竖版（默认）
  9:16  超长竖版
  1:1   正方形
  16:9  横版

示例:
  $0 generate "5个习惯让你越来越自律"
  $0 generate "今日份好心情" 1:1
  $0 balance
  $0 history 20

主页: https://xhscover.cn
EOF
}

# 主入口
case "${1:-}" in
  generate)
    generate_cover "$2" "$3"
    ;;
  balance|credits)
    get_balance
    ;;
  history)
    get_history "${2:-10}"
    ;;
  help|--help|-h)
    show_help
    ;;
  *)
    if [ -n "$1" ]; then
      generate_cover "$1" "$2"
    else
      show_help
    fi
    ;;
esac
