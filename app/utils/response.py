def success(data=None, msg='success'):
    return {
        'code': 200,
        'msg': msg,
        'data': data
    }

def fail(msg='error', code=400):
    return {
        'code': code,
        'msg': msg,
        'data': None
    }
