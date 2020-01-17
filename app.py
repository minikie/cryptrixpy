# -*- coding: utf-8 -*-
from flask import request, render_template, jsonify, send_from_directory
from flask import Flask, url_for, redirect, session, make_response, abort
import os, json, datetime
from module.database import db_session, init_db
# from module.models import Vo, UserLogin, Report
import module.dataprovider_rt as rt
import module.dataprovider_his as his


from flask_cors import CORS

app = Flask(__name__, static_folder='dist/static', template_folder='dist')

app.secret_key = 'sample_secreat_key'

# enable CORS
CORS(app)

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    #resp = make_response(render_template('index.html'))
    # resp.set_cookie('position_token', utilities.get_hash(str(random.random()),str(random.random())))
    # return resp
    return render_template('index.html')



@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/cookie')
def cookie():
    name = request.cookies.get('myname')
    return '<h1>welcome ' + name + '</h1>'



@app.route('/test')
def test_index():
    return render_template('index.html')


# 예전에 저장했던 데이터
# private로 하면 검색안됨고 email필요한걸로 redirect
@app.route('/realtimedata/<name>')
def realtimedata(name):
    if name == 'test_rdata':
        return rt.testdata()
    else:
        abort(400, 'no report exist')


@app.route('/historydata/<name>')
def historydata(name):
    if name == 'test_hdata':
        return his.testdata()
    else:
        abort(400, 'no report exist')


@app.route('/get_address_list', methods=['POST'])
def get_address_list():
    res = {}
    # post
    request_json = request.json

    print('get_address_list')
    if request.method == 'POST':
        print('post')
        print(request.json)
        keyword = request_json['keyword']
        res = utilities.get_address_list(keyword)

    return jsonify(res)


if __name__ == '__main__':
   app.run(debug = True)