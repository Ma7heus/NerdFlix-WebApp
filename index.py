from flask import Flask, render_template, redirect, request, session, url_for, flash
from Users import *
from Products import *
from Clients import *
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
    title = "BEM VINDO AO NERDFLIX!"
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

@app.route('/allproducts')
def allproducts():
    titulo = "PRODUCTS"
    listProducts = Products.getAllProducts("value")
    return render_template('products.html',titulo = titulo,listGames = listProducts)



app.run(host='0.0.0.0', port=8080, debug=True)





