from app.dao.userdao import UserDao 

def get_user_list():
    with UserDao() as user_dao:
        return user_dao.getUserList()
