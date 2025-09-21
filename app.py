from flask import Flask
from routes.disease_routes import disease_bp
from routes.case_routes import case_bp
from database.db import Base, engine
from models.case import Case
def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(disease_bp)
    app.register_blueprint(case_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
