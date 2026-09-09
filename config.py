#!/usr/bin/env python3
"""
MiMo Desktop AI Content Workflow - 配置管理
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

class ProjectConfig:
    """项目配置管理类"""
    
    def __init__(self, project_dir: Path):
        self.project_dir = Path(project_dir)
        self.config_path = self.project_dir / "config.json"
        
    def create(self, name: str, description: str = "") -> Dict[str, Any]:
        """创建新项目配置"""
        config = {
            "name": name,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "version": "1.0.0",
            "settings": {
                "default_length": 1000,
                "summary_style": "concise",
                "output_format": "markdown"
            },
            "chapters": [],
            "references": [],
            "style_samples": []
        }
        
        # 创建项目目录结构
        dirs = ["manuscripts", "outlines", "revisions", "summaries", "style_samples"]
        for d in dirs:
            (self.project_dir / d).mkdir(parents=True, exist_ok=True)
        
        # 保存配置
        self.project_dir.mkdir(parents=True, exist_ok=True)
        self.config_path.write_text(
            json.dumps(config, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        
        return config
    
    def load(self) -> Optional[Dict[str, Any]]:
        """加载项目配置"""
        if self.config_path.exists():
            return json.loads(
                self.config_path.read_text(encoding="utf-8")
            )
        return None
    
    def update(self, key: str, value: Any) -> Dict[str, Any]:
        """更新配置项"""
        config = self.load() or {}
        # 支持嵌套更新: "settings.default_length"
        keys = key.split(".")
        obj = config
        for k in keys[:-1]:
            obj = obj.setdefault(k, {})
        obj[keys[-1]] = value
        self.config_path.write_text(
            json.dumps(config, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return config

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir", type=str, required=True)
    parser.add_argument("--name", type=str, required=True)
    parser.add_argument("--description", type=str, default="")
    args = parser.parse_args()
    
    cfg = ProjectConfig(Path(args.project_dir))
    result = cfg.create(args.name, args.description)
    print(json.dumps(result, indent=2, ensure_ascii=False))
