from app.dao.userdao import UserDao
from app.utils.jwtutil import user_jwt_encode

def user_login(username, password):
    with UserDao() as user_dao:
        user = user_dao.getUserByUsername(username)
        print(f"查询到用户：{user}")
        if user and user["password"] == password:
            jwt_token = user_jwt_encode(user)
            return {
                "islogin":True,
                "token":jwt_token
            }
    return {
        "islogin":False
    }

if __name__ == "__main__":
    # 测试登录功能
    print(user_login("admin", "123456"))  # 替换为实际的用户名和密码