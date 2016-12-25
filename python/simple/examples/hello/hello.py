# -*- coding: utf8 -*-
from __future__ import unicode_literals
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! 欢迎来到FLASK世界!'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
