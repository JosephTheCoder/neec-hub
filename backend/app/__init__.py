from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from app.database import db, create_tables
import logging
import os

from flask_graphql import GraphQLView
# from .graphql import schema
from .graphql import schema

def initialize_weather_api(app): #Example code --------------
    from .weather_api import bp as weather_api
    app.register_blueprint(weather_api)

def create_app():
    app = Flask(__name__)

    env_config = Config.APP_ENV
    # app.config.from_object(config[env_config])
    app.config.from_object(Config)

    current_path = os.path.dirname(os.path.realpath(__file__))

    migrations_dir = os.path.join(current_path, 'database', 'migrations')
    Migrate(app, db, directory=migrations_dir)

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        )
    )
    
    with app.app_context():
        db.init_app(app)
        create_tables()

    CORS(app) # enable Cross-Origin Resource Sharing

    #initialize_main_api(app)
    
    return app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)