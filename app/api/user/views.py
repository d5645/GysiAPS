from flask import Blueprint, request
from app.utils.response import success, fail

user_bp = Blueprint("user", __name__)

# 注册
@user_bp.route("/register", methods=["POST"])
def register():
    return success(msg="注册成功")

# 登录
@user_bp.route("/login", methods=["POST"])
def login():
    return success(msg="登录成功")
