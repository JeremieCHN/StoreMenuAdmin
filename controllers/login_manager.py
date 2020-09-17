from flask import (session, redirect)
from settings import config
import time


class LoginManager:
    # random key -> username
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
