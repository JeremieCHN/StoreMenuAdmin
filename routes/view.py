from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for
)
from login_manager import (login_require, LoginManager)

view = Blueprint("admin", __name__)


@view.route('/login', methods=['GET'])
def login_view():
    return render_template('login.html', title="LOGIN")


@view.route('/', methods=['GET'])
@login_require
def index():
    return render_template('main.html', username = LoginManager.get_username())
