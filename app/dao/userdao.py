from .mongodao import MongoDAO

class UserDao():
    def getUserByUsername(self, username: str):
        with MongoDAO() as mongo_dao:
            collection = mongo_dao.getCollection("user")
            print(f"查询用户：{username}")
            user = collection.find_one({"username": username})
            return user
        return None
        

    def createUser(self, username: str, password: str):
        with MongoDAO() as mongo_dao:
            collection = mongo_dao.getCollection("user")
            result = collection.insert_one({"username": username, "password": password})
            return result.inserted_id
        return None

    def deleteUser(self, username: str):
        with MongoDAO() as mongo_dao:
            collection = mongo_dao.getCollection("user")
            result = collection.delete_one({"username": username})
            return result.deleted_count
        return None

    def getUserList(self):
        with MongoDAO() as mongo_dao:
            collection = mongo_dao.getCollection("user")
            users = collection.find()
            return list(users)
        return None
    
    def __enter__(self):
        """上下文管理器进入方法"""
        self.mongo_dao = MongoDAO()
        self.mongo_dao.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出方法"""
        self.mongo_dao.close()
        # 如果有异常，返回False表示继续抛出异常
        return False
    
    