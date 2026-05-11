from flask import Flask
from app.config import config

from app.api import register_blueprints

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(config[config_name])
    

    
    # 注册所有蓝图（接口）
    register_blueprints(app)
    
    return app
