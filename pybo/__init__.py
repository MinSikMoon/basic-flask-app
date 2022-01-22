from flask import Flask
app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_pybo():
        return 'hello python'
    return app