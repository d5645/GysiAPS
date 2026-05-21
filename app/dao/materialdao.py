from app.dao.mongodao import MongoDAO

class MaterialDao():
    def __init__(self):
        self.MaterialModle = {
            "FMaterialID":"",
            "FNumber": "", 
            "FName":"", 
            "FPerUnitStandHour":0.00 #标准工时，秒
            }
        
    def addMaterial(self,material):
        with MongoDAO() as mongo_dao:
            collection = mongo_dao.getCollection("material")
            result = collection.insert_one(material)
            return result.inserted_id
        return None
    