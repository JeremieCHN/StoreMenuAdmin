from flask import (session, redirect)
from functools import wraps
from settings import config
import time


def login_require(f):
    @wraps(f)
    def warpper(*args, **kwargs):
        if LoginManager.check_login():
            return f(*args, **kwargs)
        else:
            return redirect('/admin/login')
    return warpper


class LoginManager:
    login_users = {}


    @staticmethod
    def check_login():
        if 'acc' in session:
            acc = session['acc']
            if acc in LoginManager.login_users:
                return True
        return False


    @staticmethod
    def login(username, password):
        users = config['users']
        if username in users and users[username] == password:
            key = LoginManager.random_key()
            session['acc'] = key
            LoginManager.login_users[key] = username
            return True
        return False


    @staticmethod
    def logout():
        key = session['acc']
        del LoginManager.login_users[key]
        del session['acc']


    @staticmethod
    def random_key():
        return str(time.time_ns())


    @staticmethod
    def get_username():
        acc = session['acc']
        return LoginManager.login_users[acc]
