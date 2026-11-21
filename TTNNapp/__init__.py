
import os
from flask import Flask
from dotenv import load_dotenv
from .extensions import db


def create_app(test_config=None):
    load_dotenv(override=True)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "doi-secret-key-truoc-khi-deploy")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    if not app.config["SQLALCHEMY_DATABASE_URI"]:
        raise RuntimeError("DATABASE_URL is not configured.")

    db.init_app(app)

    from .routes.auth import bp as auth_bp
    from .routes.student import bp as student_bp
    from .routes.teacher import bp as teacher_bp
    from .routes.employee import bp as employee_bp
    from .routes.report import bp as report_bp
    from .routes.admin import bp as admin_bp
    blueprints = (auth_bp, student_bp, teacher_bp, employee_bp, report_bp, admin_bp)
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
