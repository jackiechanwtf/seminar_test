from flask import Flask

from src.auth.routes import auth_bp
from src.market.routes import market_bp


def create_app():
    app = Flask(__name__)
    app.secret_key = "my-secret-key"
    app.config["DB_CONFIG"] = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "root",
        "db": "test_db",
    }

    app.register_blueprint(market_bp, url_prefix="/market")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    @app.route("/")
    def index_handler():
        return "Hello world"

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5001)
