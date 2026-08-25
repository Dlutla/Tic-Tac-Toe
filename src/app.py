"""
Основной файл приложения. Создаёт Flask-приложение, настраивает зависимости и запускает сервер.
"""
from flask import Flask
from di.container import Container
from web.controller.game_controller import game_bp

def create_app():
    app = Flask(__name__)

    container = Container()

    app.config['GAME_SERVICE'] = container.game_service
    app.config['GAME_REPO'] = container.repository

    app.register_blueprint(game_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)