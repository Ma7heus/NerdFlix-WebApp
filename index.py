from flask import Flask, render_template, redirect, request
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
    proxima = request.args.get('proxima')
    return render_template("login.html",title=title)

@app.route('/autenticar', method=['POST', ])
def autenticar():
    


    return redirect('/login')








app.run(host='0.0.0.0', port=8080, debug=True)




