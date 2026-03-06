from flask import Flask
from Src.Api.Database import db
from Src.Api.Routes.product_routes import product_bp
from Routes.auth_routes import auth_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://postgres:030205@localhost:5432/postgres?client_encoding=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(product_bp, url_prefix="/v1")
    app.register_blueprint(auth_bp, url_prefix="/v1")

    @app.route("/health")
    def health():
        return {"status": "API running"}

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)