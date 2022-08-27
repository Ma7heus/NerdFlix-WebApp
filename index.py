from flask import Flask, render_tamplate, redirect
from Clients import *
from Products import *
from Users import *

app = Flask(__name__)

@pp.route('/')
def index():
    title = "Bem vindo ao NerdFlix!"
    return render_template("index.html", title=title)




app.run(debuger=True)




