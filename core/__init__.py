from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .extensions import db, migrate
from .models import Recipe

import os

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DB_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        FLASK_ADMIN_SWATCH='cerulean',
    )
    db.init_app(app)
    migrate.init_app(app, db)

    admin = Admin(app, template_mode='bootstrap3', name='Recipe Admin')
    admin.add_view(ModelView(Recipe, db.session))

    from .routes import main, product
    app.register_blueprint(main)
    app.register_blueprint(product)

    return app

