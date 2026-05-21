from app.dao.mongodao import MongoDAO

def add_material(material):
    if material_validate(material)[0]:
        with MongoDAO() as mongo_dao:
            collection = mongo_dao.getCollection("material")
            result = collection.insert_one(material) 
            return result.inserted_id
    return None

def material_validate(material):
    if not "FMaterialID" in material or not material["FMaterialID"]:
        return False, "物料ID不能为空"
    if not "FNumber" in material or not material["FNumber"]:
        return False, "物料编号不能为空"
    if not "FName" in material or not material["FName"]:
        return False, "物料名称不能为空"
    if not isinstance(material["FPerUnitStandHour"], (int, float)):
        return False, "标准工时必须是数字"
    return True, ""