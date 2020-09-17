import os
from datetime import timedelta
from flask import (Flask, url_for)
from settings import config
from routes import (view_blueprint, apis_blueprint)

app = Flask(__name__)

# 重载url_for，在输出的URL后面带上?q=1
# 实现静态文件的更新而不用考虑html缓存过期时间
@app.context_processor
def override_url_for():
    return dict(date_url_for=date_url_for)


def date_url_for(endpoint, **value):
    if endpoint == 'static':
        filename = value.get('filename', None)
    if filename:
        file_path = os.path.join(app.root_path, endpoint, filename)
        value['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **value)


if __name__ == '__main__':
    # session的秘钥
    app.secret_key = config['secret_key']

    # 启用模板文件的热更
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.register_blueprint(view_blueprint, url_prefix='/admin')
    app.register_blueprint(apis_blueprint, url_prefix='/api')
    host = config['HOST']
    port = config['PORT']
    app.run(host, port)
