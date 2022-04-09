from flask import Flask
from flask import render_template,Response

app = Flask(__name__)

@app.route('/',methods=['GET','PUT','OPTIONS'])
def hellow_world():
    resp = Response("SUCCESS")
    # resp.set_cookie('token','12345')
    resp.headers['Access-Control-Allow-Origin'] = '127.0.0.1:8000'
    resp.headers['Access-Control-Allow-Methods'] = '*'
    # resp.headers['Access-Control-Max-Age'] = '600'
    return resp

@app.route("/auth",methods=['GET'])
def cors():
    resp = Response("Авторизовано")
    resp.set_cookie('token', '12345')
    return resp

# @app.route("/",methods=['GET'])
# def cors():
#     resp = Response("")
#     resp.headers['Access-Control_Allow-Origin'] = '*'
#     resp.headers['Access-Control-Allow-Methods'] = '*'
#     return resp