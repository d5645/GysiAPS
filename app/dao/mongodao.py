# MongoDB Dao 层

from pymongo import MongoClient
import pymongo
from pymongo.errors import PyMongoError
from typing import Dict, List, Optional, Any

class MongoDAO():
    def __init__(self, host: str = 'localhost', port: int = 27017, 
                 username: Optional[str] = None, db_name: str = "system",
                 password: Optional[str] = None, auth_source: str = 'admin'):
        """
        初始化MongoDB连接
         
        :param host: MongoDB主机地址
        :param port: MongoDB端口号
        :param db_name: 数据库名称
        :param username: 用户名（可选）
        :param password: 密码（可选）
        :param auth_source: 认证数据库
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.auth_source = auth_source
        self.client = None
        self.db_name = db_name
        self.db = None
    
    def connect(self) -> None:
        """建立数据库连接"""
        try:
            # 创建客户端连接
            if self.username and self.password:
                self.client = MongoClient(
                    host=self.host,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                    authSource=self.auth_source
                )
            else:
                self.client = MongoClient(self.host, self.port)
            
            # 验证连接
            self.client.admin.command('ping')
            # 获取数据库对象
            self.db = self.client[self.db_name]
            print(f"成功连接到MongoDB数据库: {self.db_name}")
        except PyMongoError as e:
            print(f"连接MongoDB失败: {str(e)}")
            raise
    
    def close(self) -> None:
        """关闭数据库连接"""
        if self.client:
            self.client.close()
            print("MongoDB连接已关闭")
            self.client = None
            self.db = None
    
    def getCollection(self, collection_name: str) :
        if self.db is None: # type: ignore
            print("数据库未连接")
            return None
        try:
            return self.db[collection_name]
        except PyMongoError as e:
            print(f"无法连接至集合{collection_name}: {str(e)}")
        
    def __enter__(self):
        """上下文管理器进入方法"""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出方法"""
        self.close()
        # 如果有异常，返回False表示继续抛出异常
        return False
    
if __name__ == "__main__":
    try:
        with MongoDAO() as mDao:
            sys_user = mDao.getCollection("sys_user")
            result = sys_user.find({"username":"admin"}) # type: ignore
            for f in result:
                print(f)
    except Exception as e:
        print("error")
        raise Exception("Error find documents:",e)