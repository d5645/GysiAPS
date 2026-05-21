from flask import Blueprint, request
from app.utils.response import success, fail
from app.service.base.material_service import add_material

base_bp = Blueprint("material", __name__)

@base_bp.route("/add", methods=["POST"])
def add_material_route():
    material = request.get_json()
    if add_material(material):
        return success(msg="添加物料成功")
    else:
        return fail(msg="添加物料失败")

