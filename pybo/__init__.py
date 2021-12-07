from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# 전역 변수로 객체 생성
db = SQLAlchemy()
migrate = Migrate()

# create_app 함수가 애플리케이션 팩토리다.
# app 객체를 전역으로 사용할 때 발생하는 문제를 예방
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    #ORM
    # 객체 초기화
    db.init_app(app)
    migrate.init_app(app,db)
    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)
    #
    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app