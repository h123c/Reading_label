# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 22:43
# @Author  : hc
from flask_script import Manager

from app.utils.config import create_app

app = create_app()

manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()

