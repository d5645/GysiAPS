from app.api.user.views import user_bp
from app.api.base.views import base_bp
from app.api.material.views import base_bp as material_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix="/api/user")
    app.register_blueprint(base_bp, url_prefix="/api/base")
    app.register_blueprint(material_bp, url_prefix="/api/material")
    