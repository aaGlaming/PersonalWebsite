# -*- coding: utf-8 -*-
"""把 data/resume_data.py 导出为静态 JSON，供纯静态托管（EdgeOne Pages 等）使用。

用法：python export_data.py
输出：frontend/public/data/{profile,skills,projects,education}.json
改完简历数据后：先跑本脚本，再 npm run build。
"""
import json
import os

from data import resume_data

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend", "public", "data")

FILES = {
    "profile.json": resume_data.PROFILE,
    "skills.json": resume_data.SKILLS,
    "projects.json": resume_data.PROJECTS,
    "education.json": {**resume_data.EDUCATION, "honors": resume_data.HONORS},
}


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    for name, payload in FILES.items():
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        print("written:", os.path.relpath(path, os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    main()
