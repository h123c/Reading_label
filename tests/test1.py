# -*- coding: utf-8 -*-
# @Time    : 2018/11/13 22:43
# @Author  : hc
from flask import Flask
from flask import request
from flask import render_template
import os
root_path = os.getcwd()


app = Flask(__name__)

@app.route('/',methods=['GET','POSt'])
def index():
    return render_template("index.html")

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In </button></p>
    </form>
    '''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello ,admin!</h3>'
    return '<h3>Bad username or password</h3>'



@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html')

if __name__ == '__main__':
    app.run()