from app.api.user.views import user_bp

def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix="/api/user")
    