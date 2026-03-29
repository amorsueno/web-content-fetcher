# web-content-fetcher

网页正文提取工具，支持 OpenClaw / Claude Code / Codex 等平台。

## 文件结构

```
web-content-fetcher/
├── SKILL.md          # 跨平台 skill 描述文件
├── README.md         # 本文件
├── requirements.txt  # Python 依赖
└── scripts/
    ├── fetch.py      # Scrapling + html2text 提取脚本
    └── fetch_simple.py # 简化版（urllib + html2text）
```

## 安装

1. 克隆仓库：
   ```bash
   git clone <repo-url>
   cd web-content-fetcher
   ```

2. 安装 Python 依赖：
   ```bash
   pip install scrapling html2text --break-system-packages
   ```

## 使用方式

### 命令行

```bash
python3 scripts/fetch.py <url> [max_chars]
```

示例：
```bash
python3 scripts/fetch.py https://mp.weixin.qq.com/s/xxx 30000
```

输出为干净的 Markdown 正文，可重定向到文件：

```bash
python3 scripts/fetch.py <url> > output.md
```

### OpenClaw

将整个目录放到 OpenClaw workspace skills 目录，重启后自动生效。

### Claude Code

将 `SKILL.md` 内容添加到 Claude Code 的 custom_skill 或项目中，或将整个目录作为项目工作目录，Claude Code 会自动读取 `SKILL.md` 作为 skill 定义。

## 支持平台

| 平台 | 方案 | 状态 |
|------|------|------|
| 微信公众号 | Scrapling | ✅ |
| Substack | Scrapling / Jina | ✅ |
| Medium | Scrapling / Jina | ✅ |
| GitHub | web_fetch | ✅ |
| 知乎 | Scrapling | ✅ |
| CSDN | Scrapling | ✅ |
| 小红书 | ❌ 需登录态 | ❌ |

## 提取效果

返回标准 Markdown，保留：
- 标题层级（`# ## ###`）
- 超链接 `[文字](url)`
- 图片 `![alt](url)`
- 列表、代码块、引用块
