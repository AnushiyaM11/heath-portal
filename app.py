from flask import Flask
from config import Config
from extensions import init_extensions, db
from flask_cors import CORS
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"], supports_credentials=True)
    app.config.from_object(Config)

    init_extensions(app)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all() 

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
