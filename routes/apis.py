from functools import wraps
import json
from flask import (
    request,
    Blueprint
)
from controllers.login_manager import LoginManager
import controllers.menu_manager as MenuManager
import errcode

api = Blueprint('api', __name__)


def login_require(f):
    @wraps(f)
    def warpper(*args, **kwargs):
        if LoginManager.check_login():
            return f(*args, **kwargs)
        else:
            return __resp(errcode.NEED_LOGIN)
    return warpper


def __resp(_errcode=errcode.OK, data_str=''):
    return json.dumps({ 'code': _errcode, 'data': data_str })


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

@api.route('/get_data', methods=['GET'])
# @login_require
def get_data():
    return __resp(data_str = json.dumps(MenuManager.get_data()))


@api.route('/upload_img', methods=['POST'])
@login_require
def api_upload_img():
    img = request.files.get('file')
    if not img:
        return __resp(errcode.NO_IMAGE)
    MenuManager.add_image(img)
    return __resp()


@api.route('/add_type', methods=['POST'])
# @login_require
def api_add_type():
    # MenuManager.add
    pass
