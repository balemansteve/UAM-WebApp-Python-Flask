#!/usr/bin/env python3


import sys
import json

from flask import Flask, request, render_template, url_for, session
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/home', methods=['GET'])
def home():
    return app.send_static_file('home.html')


@app.route('/login', methods=['GET'])
def login():
    return app.send_static_file('login.html')


@app.route('/signup', methods=['GET'])
def signup():
    return app.send_static_file('signup.html')


@app.route('/agent', methods=['GET'])
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/processSignup', methods=['POST'])
def processSignup():
    missing = []
    fields = ['nickname', 'email', 'passwd', 'confirm', 'signup_submit']
    for field in fields:
        valor = request.form.get(field, None)
        if valor is None or valor == "":
            missing.append(field)
    if missing:
        return render_template("missingFields.html", inputs=missing, next=url_for("signup"))
    return '<!DOCTYPE html> ' \
           '<html lang="es">' \
           '<head>' \
           '<link href="static/css/my-socnet-style.css" rel="stylesheet" type="text/css"/>' \
           '<title> Home - SocNet </title>' \
           '</head>' \
           '<body> <div id ="container">' \
           '<a href="/"> SocNet </a> | <a href="home"> Home </a> | <a href="login"> Log In </a> | <a href="signup"> Sign Up </a>' \
           '<h1>Data from Form: Sign Up</h1>' \
           '<form><label>Nickame: ' + request.form['nickname'] + \
        '</label><br><label>email: ' + request.form['email'] + \
        '</label><br><label>passwd: ' + request.form['passwd'] + \
        '</label><br><label>confirm: ' + request.form['confirm'] + \
        '</label></form></div></body>' \
        '</html>'

def process_error(message, next_page):
    """

    :param message:
    :param next_page:
    :return:
    """
    return render_template("error.html", error_message=message, next=next_page)
'''
# open json and create an instance that is storage in the variable data as a dictionary
with open("Data/users.json", "r") as f:
    data = json.load(f)

# write data in json file
datos = {
    "user_name": "James",
    "password": "007",
    "messages": [(1532648502.113984, "mensaje 1"), (1532648642.729385,     "mensaje 1")],
    "email": session['email'],
    "friends": session['friends']
}

with open("data/james.bond@mi6.uk", 'w') as f:
    json.dump(datos, f)
'''
# start the server with the 'run()' method
if __name__ == '__main__':
    if sys.platform == 'darwin':  # different port if running on MacOsX
        app.run(debug=True, port=8080)
    else:
        app.run(debug=True, port=5000)