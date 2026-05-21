from flask import Blueprint, request
from app.utils.response import success, fail
from app.service.user.user_service import get_user_list
from app.service.base.user_login import user_login

user_bp = Blueprint("user", __name__)

# 注册
@user_bp.route("/register", methods=["POST"])
def register():
    return success(msg="注册成功")

# 登录
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    res = user_login(username, password)
    if res["islogin"]:
        return success(msg="登录成功", data={"token": res["token"]})
    else:
        return fail(msg="用户名或密码错误")

@user_bp.route("/list", methods=["GET"])
def get_user_list():
    user_list = get_user_list()
    return success(data=user_list)