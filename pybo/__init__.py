from flask import Flask

def create_app(): #flask의 내장함수, 첫시작
    app = Flask(__name__) #flask앱인 app을 만든다. 
    from .views import main_views #views 디렉터리의 main_views 코드를 import
    app.register_blueprint(main_views.bp) #app(flask앱객체)에 블루 프린트 객체인 bp를 등록한다. 
    return app #app을 return한다. 