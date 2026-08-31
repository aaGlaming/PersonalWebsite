import os

from flask import Flask, jsonify, send_from_directory

from routes import api, data_bp

FRONTEND_DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend", "dist")


def create_app() -> Flask:
    app = Flask(__name__, static_folder=None)
    app.register_blueprint(api)
    app.register_blueprint(data_bp)

    @app.errorhandler(404)
    def not_found(_e):
        # API 未命中返回 JSON，页面路由回退到前端 SPA
        if os.path.isdir(FRONTEND_DIST):
            return send_from_directory(FRONTEND_DIST, "index.html")
        return jsonify({"error": "Not Found"}), 404

    @app.get("/")
    def index():
        if os.path.isdir(FRONTEND_DIST):
            return send_from_directory(FRONTEND_DIST, "index.html")
        return jsonify({"message": "frontend/dist 不存在，请先执行 npm run build"})

    @app.get("/<path:path>")
    def static_files(path: str):
        full = os.path.join(FRONTEND_DIST, path)
        if os.path.isfile(full):
            return send_from_directory(FRONTEND_DIST, path)
        return not_found(None)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
