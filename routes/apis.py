from flask import (
    request,
    Blueprint
)
import json
from login_manager import (login_require, LoginManager)

api = Blueprint('api', __name__)


def __resp(err_name='success', data_str=''):
    errcode = {
        'success': 0,
        'no_login': 1,
        'login_err': 2
    }
    return json.dumps({ 'code': errcode[err_name], 'data': data_str })


@api.route('/login', methods=['POST'])
def api_login():
    data = json.loads(request.data)
    if 'username' in data and 'password' in data:
        if LoginManager.login(data['username'], data['password']):
            return __resp()
    return __resp('login_err')


@api.route('logout', methods=['GET'])
@login_require
def api_logout():
    LoginManager.logout()
    return __resp()


# TODO upload image
@api.route('upload_img', methods=['POST'])
@login_require
def api_upload_img():
    return "UPLOAD IMG"
