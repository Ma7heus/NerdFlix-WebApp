from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bem vindo ao NerdFlix!</h1>'




app.run(host='0.0.0.0', port=8080, debug=True)




