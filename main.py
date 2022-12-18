from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_mananger = LoginManager()
def app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    login_mananger.init_app(app)
    login_mananger.login_view = "/login"

    db.init_app(app)

    from index.index import index_bp
    app.register_blueprint(index_bp)

    from login.login import login_bp
    app.register_blueprint(login_bp)

    from register.register import register_bp
    app.register_blueprint(register_bp)

    with app.app_context():
        db.create_all()

    return app

from model import *

if __name__ == "__main__":
    app().run(host="0.0.0.0", port=5000)