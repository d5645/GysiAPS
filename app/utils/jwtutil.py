import jwt
import time

def user_jwt_encode(user):
    now_time = int(time.time())
    payload = {
        'username': user["username"],
        "efficacy": now_time,
        "expire": now_time + 3600 * 24  # 设置过期时间为24小时
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    print(f"生成的JWT：{token}")
    return token