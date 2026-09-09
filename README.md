# MiMo Desktop AI 内容创作工作流

**一个基于 MiMo Desktop 构建的本地化 AI 内容创作工作站**，致力于用自然语言和多轮对话替代繁杂的菜单操作。

---

## 项目背景

作者日常使用 AI 编程智能体（ZCode / DeepSeek）处理复杂的软件工程任务：
- 多步骤代码重构 · 跨文件批量修改 · 自动化测试生成 · 项目架构分析

将这种「以自然语言驱动真实创作」的模式，**延伸到多文档内容创作** ——
从素材整理 → 智能草稿 → 审校 → 排版 → 输出，整个流程都在本地完成。

MiMo Desktop 正好提供了：
- **长上下文窗口**：整本手稿作为上下文，AI 理解全局结构
- **本地优先**：未发表稿件不上传云端，保护知识产权
- **离线可用**：不依赖网络波动，随时沉浸创作
- **多轮对话式交互**：人机实时迭代，而非一次性输出

---

## 功能特性

### 1. 文档编排 `outline`
输入主题或大纲要点，AI 自动生成结构化 Markdown 大纲。

### 2. 章节摘要 `summarize`
对长文档进行智能摘要，提取关键信息，保持原文脉络。

### 3. 修订对比 `diff`
将多个版本的草稿进行对比，直观展示改动之处，便于接受/拒绝修改。

### 4. 风格模仿 `imitate`
输入参考段落，AI 生成与其风格一致的新内容，维持全文语气统一。

### 5. 智能排版 `format`
根据目标平台（微信 / 知乎 / 博客）自动调整排版格式。

---

## 快速开始

```bash
# 克隆项目
git clone https://github.com/[你的用户名]/mimo-desktop-ai-workflow.git
cd mimo-desktop-ai-workflow

# 安装依赖
pip install -r requirements.txt

# 查看帮助
python main.py --help
```

---

## 使用示例

```bash
# 初始化项目目录
python main.py init --project my-wechat-article

# 生成文章大纲
python main.py outline --topic "AI辅助写作的未来" --output outline.md

# 编写第一章内容
python main.py write --outline outline.md --chapter "引言" --length 800

# 摘要生成
python main.py summarize --doc manuscripts/intro.md --style "简介"

# 对比修订
python main.py diff --file-a revisions/v1.md --file-b revisions/v2.md

# 风格模仿
python main.py imitate --sample samples/formal_style.md --topic "科技趋势"

# 导出为指定格式
python main.py format --input final.md --platform wechat
```

---

## 在 MiMo Desktop 中的价值

| 传统方式 | MiMo Desktop 工作流 |
|---|---|
| 多次复制粘贴到网页 AI | 整个项目文件夹常驻上下文 |
| 每次对话都要重新解释背景 | 多轮对话保持上下文连贯 |
| 文件通过邮箱/网盘传输 | 本地存储，隐私有保障 |
| 依赖网络环境，偶有中断 | 离线可用，创作不打断 |
| 输出后手动整理修改 | AI 实时协作，修改即保存 |

---

## 目录结构

```
mimo-desktop-ai-workflow/
├── main.py              # 主命令行入口
├── workflow.py          # 核心工作流逻辑
├── config.py            # 项目配置管理
├── requirements.txt     # Python 依赖
├── README.md            # 项目说明 (本文件)
├── examples/            # 示例数据
│   ├── sample_outline.md
│   └── sample_style.md
├── projects/            # 用户项目目录 (运行时生成)
│   ├── my-wechat-article/
│   │   ├── manuscripts/
│   │   ├── outlines/
│   │   ├── revisions/
│   │   ├── summaries/
│   │   └── style_samples/
└── output/              # 生成内容存放
```

---

## 关于作者

该项目由一个热爱折腾 AI 工具的开发者创建。
日常使用 DeepSeek / GPT / Claude 等多款 AI 编程助手，
热衷于用自然语言驱动复杂的工程任务，
并探索如何将这种模式应用于内容创作领域。

通过 MiMo Desktop Beta 计划，
希望将这个工作流落地到一个真正的桌面应用中，
让写作者 / 内容创作者也能体验到「像编程一样写作」的乐趣。
