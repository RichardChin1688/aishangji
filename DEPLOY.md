# 启橙 AI 官网 - 部署指南

## 快速部署到 GitHub Pages

### 1. 创建 GitHub 仓库

访问 https://github.com/new 创建新仓库，例如：`qicheng-ai-web`

### 2. 推送代码

在项目目录下执行：

```bash
cd /home/richardchin/.openclaw/workspace/desktop/qicheng-ai-website

# 初始化 git
git init

# 添加所有文件
git add .

# 提交
git commit -m "启橙 AI 官网初始化"

# 创建主分支
git branch -M main

# 关联远程仓库 (替换为你的仓库地址)
git remote add origin https://github.com/YOUR_USERNAME/qicheng-ai-web.git

# 推送
git push -u origin main
```

### 3. 启用 GitHub Pages

1. 进入 GitHub 仓库页面
2. 点击 **Settings** → **Pages**
3. Source 选择 **Deploy from branch**
4. Branch 选择 **main**，文件夹选择 **/ (root)**
5. 点击 **Save**

等待 1-2 分钟，网站将发布在：
```
https://YOUR_USERNAME.github.io/qicheng-ai-web/
```

### 4. 自定义域名 (可选)

如需使用自定义域名（如 `www.qichengai.com`）：

1. 在 GitHub Pages 设置中添加自定义域名
2. 在域名服务商处配置 CNAME 记录指向 `YOUR_USERNAME.github.io`

---

## 网站页面

| 页面 | 文件 | 说明 |
|------|------|------|
| 首页 | `index.html` | 企业全域增长赋能生态总览 |
| 技术服务 | `technical.html` | AI 技术服务目录（增长拓客/降本增效/增值上市） |
| AI 私董会 | `private-board.html` | 生态合伙人分润权益 |
| OPC 孵化 | `opc-incubator.html` | 城市合伙人计划（阶梯分红 + 投资标准） |
| AI 商学院 | `business-school.html` | 企业团队 AI 培训赋能 |
| 联系我们 | `contact.html` | 商务合作联系方式 |

---

## 优化说明

✅ **简化内容** - 移除冗长文案，保留核心价值点
✅ **修正数据** - 统一分润比例（10%/15%/20%）和投资标准
✅ **移除交互** - 删除模态框、表单提交等动态功能
✅ **静态部署** - 适配 GitHub Pages 静态托管
✅ **精简结构** - 移除悬浮按钮、复杂动画等不必要元素

---

## 后续更新

如需更新网站内容：

```bash
# 修改文件后
git add .
git commit -m "更新内容说明"
git push
```

GitHub Pages 会自动重新部署（通常 1-2 分钟生效）。

---

**技术支持**: 联系启橙 AI 技术团队
**版本**: v1.0 - 2026 年 7 月
