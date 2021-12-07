from flask import Flask
app = Flask(__name__) # __name__ = 모듈명 여기서는 pybo

@app.route('/')
def hello_pybo():
    return "Hello, Pybo!"