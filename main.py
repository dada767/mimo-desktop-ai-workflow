#!/usr/bin/env python3
"""
MiMo Desktop AI 内容创作工作流 - 主程序入口
基于自然语言交互的多文档内容创作工作站
"""

import sys
import os
import json
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))

from workflow import Workflow
from config import ProjectConfig


def show_help():
    help_text = """
MiMo Desktop AI 内容创作工作流

使用方法:
  python main.py <命令> [参数]

可用命令:
  init <项目名>          初始化新项目
  outline <主题>         生成文章大纲
  summarize <章节>       生成章节摘要
  diff <文件A> <文件B>   对比两个版本
  imitate <样本> <主题>  风格模仿
  format <文件>          格式化输出
  help                   显示此帮助信息
  version                显示版本信息
"""
    print(help_text)


def cmd_init(args):
    project_name = args[0] if args else "my-project"
    project_dir = Path.cwd() / project_name
    config = ProjectConfig(project_dir)
    result = config.create(project_name)
    print(f"✓ 项目初始化成功: {project_name}")
    print(f"  位置: {project_dir}")
    for d in ["manuscripts", "outlines", "revisions", "summaries", "style_samples"]:
        print(f"  - {d}/")


def cmd_outline(args):
    topic = " ".join(args) if args else "我的文章主题"
    w = Workflow(Path.cwd())
    outline = w.generate_outline(topic)
    md = f"# {outline['topic']}\n\n"
    for sec in outline["sections"]:
        md += f"## {sec}\n\n"
    out_dir = Path.cwd() / "outlines"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{topic.replace(' ', '_')}.md"
    path.write_text(md, encoding="utf-8")
    print(f"✓ 大纲已生成: {path}")
    print(md)


def cmd_summarize(args):
    chapter = args[0] if args else "content.md"
    path = Path.cwd() / "manuscripts" / chapter
    if not path.exists():
        print(f"✗ 文件不存在: {path}")
        return
    content = path.read_text(encoding="utf-8")
    w = Workflow(Path.cwd())
    summary = w.summarize(content)
    sdir = Path.cwd() / "summaries"
    sdir.mkdir(parents=True, exist_ok=True)
    out = sdir / f"{chapter.replace('.md','')}_summary.json"
    out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ 摘要已生成: {out}")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


def cmd_diff(args):
    if len(args) < 2:
        print("用法: python main.py diff <文件A> <文件B>")
        return
    w = Workflow(Path.cwd())
    v1 = (Path.cwd() / args[0]).read_text(encoding="utf-8")
    v2 = (Path.cwd() / args[1]).read_text(encoding="utf-8")
    result = w.diff_versions(v1, v2)
    rdir = Path.cwd() / "revisions"
    rdir.mkdir(parents=True, exist_ok=True)
    out = rdir / f"diff_{args[0]}_vs_{args[1]}.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ 差异分析已生成: {out}")
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_imitate(args):
    if len(args) < 2:
        print("用法: python main.py imitate <样本> <主题>")
        return
    sample = args[0]
    topic = " ".join(args[1:])
    spath = Path.cwd() / "style_samples" / sample
    if not spath.exists():
        print(f"✗ 样本文件不存在: {spath}")
        return
    content = spath.read_text(encoding="utf-8")
    w = Workflow(Path.cwd())
    output = w.imitate_style(content, topic)
    out_dir = Path.cwd() / "style_samples"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"imitated_{sample}"
    out.write_text(output, encoding="utf-8")
    print(f"✓ 风格模仿已完成: {out}")
    print(output)


def cmd_format(args):
    if not args:
        print("用法: python main.py format <输入文件>")
        return
    inp = Path.cwd() / args[0]
    if not inp.exists():
        print(f"✗ 文件不存在: {inp}")
        return
    content = inp.read_text(encoding="utf-8")
    lines = [l.strip() for l in content.split("\n")]
    out_dir = Path.cwd() / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{inp.stem}_formatted.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ 格式化完成: {out}")
    print("\n".join(lines[:8]))


def main():
    if len(sys.argv) < 2:
        show_help()
        return
    command = sys.argv[1].lower()
    args = sys.argv[2:]
    commands = {
        "help": show_help,
        "version": lambda: print("v1.0.0"),
        "init": cmd_init,
        "outline": cmd_outline,
        "summarize": cmd_summarize,
        "diff": cmd_diff,
        "imitate": cmd_imitate,
        "format": cmd_format,
    }
    if command == "help":
        show_help()
    elif command == "version":
        print("v1.0.0")
    elif command in commands:
        commands[command](args)
    else:
        print(f"✗ 未知命令: {command}")
        show_help()


if __name__ == "__main__":
    main()
