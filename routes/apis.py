from functools import wraps
import json
import os
from flask import (
    request,
    Blueprint,
    send_file,
    abort
)
from controllers.login_manager import LoginManager
import controllers.menu_manager as MenuManager
from settings import config
import errcode

def login_require(f):
    @wraps(f)
    def warpper(*args, **kwargs):
        # if LoginManager.check_login():
        #     return f(*args, **kwargs)
        # else:
        #     return __resp(errcode.NEED_LOGIN)
        return f(*args, **kwargs)
    return warpper

def __resp(_errcode=errcode.OK, data_str=''):
    return json.dumps({ 'code': _errcode, 'data': data_str })


api = Blueprint('api', __name__)

# 拉取数据相关的，对外也使用的
@api.route('/get_data', methods=['GET'])
def get_data():
    f = open(config['data_file'], 'r')
    d = f.read()
    f.close()
    return __resp(data_str = d)

@api.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    filename = os.path.join(config['image_path'], filename)
    if not os.path.exists(filename):
        return abort(404)
    return send_file(filename)

# 登录相关的
@api.route('/login', methods=['POST'])
def api_login():
    data = json.loads(request.data)
    if 'username' in data and 'password' in data:
        if LoginManager.login(data['username'], data['password']):
            return __resp()
    return __resp(errcode.LOGIN_FAILED)

@api.route('/logout', methods=['GET'])
@login_require
def api_logout():
    LoginManager.logout()
    return __resp()

# 管理相关的
@api.route('/upload_img', methods=['POST'])
@login_require
def api_upload_img():
    img = request.files.get('file')
    if not img:
        return __resp(errcode.NO_IMAGE)
    MenuManager.add_image(img)
    return __resp()

@api.route('/add_type', methods=['POST'])
@login_require
def api_add_type():
    pass

@api.route('/rm_type', methods=['GET'])
@login_require
def api_rm_type():
    pass

@api.route('/add_goods', methods=['POST'])
@login_require
def api_add_goods():
    pass
