from flask import Flask, render_template, current_app as app

app = Flask(__name__)

@app.route('/')
def index():
        return "Welcome to Nana's Rainbow project"

@app.route('/red')
def red():
        name ="red"
        background = "#FF0000"
        return render_template('rainbow.html', name =$
        
@app.route('/orange')
def orange():
        name ="orange"
        background = "orange"
        return render_template('rainbow.html', name =$

@app.route('/yellow')
def yellow():
        name ="yellow"
        background = "yellow"
        return render_template('rainbow.html', name =$
        
@app.route('/green')
def green():
        name ="green"
        background = "green"
