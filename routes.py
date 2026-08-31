# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify

from data import resume_data

api = Blueprint("api", __name__, url_prefix="/api")
data_bp = Blueprint("data", __name__)


@api.get("/profile")
def profile():
    return jsonify(resume_data.PROFILE)


@api.get("/skills")
def skills():
    return jsonify(resume_data.SKILLS)


@api.get("/projects")
def projects():
    return jsonify(resume_data.PROJECTS)


@api.get("/education")
def education():
    return jsonify({**resume_data.EDUCATION, "honors": resume_data.HONORS})


# 与静态托管的 /data/*.json 文件路径保持一致，前端两种模式通用
DATA_FILES = {
    "profile": lambda: resume_data.PROFILE,
    "skills": lambda: resume_data.SKILLS,
    "projects": lambda: resume_data.PROJECTS,
    "education": lambda: {**resume_data.EDUCATION, "honors": resume_data.HONORS},
}


@data_bp.get("/data/<name>.json")
def data_json(name: str):
    factory = DATA_FILES.get(name)
    if factory is None:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(factory())
