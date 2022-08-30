<<<<<<< HEAD
from flask import Flask, render_template, redirect, request, session, url_for, flash
from Users import *
from Products import *
from Clients import *
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bem vindo ao NerdFlix!</h1>'

@app.route('/login')
def login():
    title = "FAÇA O SEU LOGIN"
    #proxima = request.args.get('proxima')
    return render_template("login.html",title=title)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    listNickName = Users.getNickName()
    userName = request.form['userName']
    if userName in listNickName:
        userPassword = Users.getUserPassword(userName)
        if request.form['userPassword'] == userPassword:
            return redirect('/')
        else:
            return redirect('login')
=======
from flask import Flask, render_tamplate, redirect
from Clients import *
from Products import *
from Users import *

app = Flask(__name__)

@pp.route('/')
def index():
    title = "Bem vindo ao NerdFlix!"
    return render_template("index.html", title=title)
>>>>>>> 16a9bbb3cb1711c3af44da74c8647fb986779ad4




<<<<<<< HEAD





app.run(host='0.0.0.0', port=8080, debug=True)
=======
app.run(debuger=True)
>>>>>>> 16a9bbb3cb1711c3af44da74c8647fb986779ad4




