from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)  
    migrate.init_app(app,db)

    first_request_handled = False 
    @app.before_request
    def before_first_request():
        nonlocal first_request_handled
        if not first_request_handled:
            from app.seeds_unko import register_first_unko
            register_first_unko()
            first_request_handled = True

    from app.routes.routes import bp as api_bp  
    app.register_blueprint(api_bp, url_prefix='/api')  

    return app

