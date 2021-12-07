from flask import Flask

# create_app 함수가 애플리케이션 팩토리다.
# app 객체를 전역으로 사용할 때 발생하는 문제를 예방
def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)
    #
    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, Pybo!'

    return app