from functools import wraps
from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for
)
from controllers.login_manager import LoginManager

view = Blueprint("admin", __name__)

def login_require(f):
    @wraps(f)
    def warpper(*args, **kwargs):
        if LoginManager.check_login():
            return f(*args, **kwargs)
        else:
            return redirect('/admin/login')
    return warpper

@view.route('/login', methods=['GET'])
def login_view():
    return render_template('login.html', title="LOGIN")


@view.route('/', methods=['GET'])
@login_require
def index():
    return redirect('/admin/good')

@view.route('/img', methods=['GET'])
@login_require
def img_view():
    return render_template('main.html', username = LoginManager.get_username(), choise=1)

@view.route('/type', methods=['GET'])
@login_require
def type_view():
    return render_template('main.html', username = LoginManager.get_username(), choise=2)

@view.route('/good', methods=['GET'])
@login_require
def good_view():
    return render_template('main.html', username = LoginManager.get_username(), choise=3)

