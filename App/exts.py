from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_restful import Api
from flask_cors import CORS
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config={
    'CACHE_TYPE': 'simple',
})
api = Api()
cors = CORS(resources={r"/*": {"origins": "*"}})
mail = Mail()


def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    cache.init_app(app=app)
    api.init_app(app=app)
    cors.init_app(app=app)
    mail.init_app(app=app)


