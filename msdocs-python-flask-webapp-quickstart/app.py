import os
import math

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    valor_a = float(request.form.get('valor-a'))
    valor_b = float(request.form.get('valor-b'))
    op = request.form.get('operacao')

    if op == "+":
        result = valor_a + valor_b
    if op == "-":
        result = valor_a - valor_b
    if op == "*":
        result = valor_a * valor_b     
    if op == "/":
        if valor_b > 0:
            result = valor_a / valor_b
        else:
            result = "Este valor não é divisível"
        
    if op == "//":
        result = valor_a // valor_b
    if op == "**":
        result = valor_a ** valor_b  
    if op == "***":
        result = math.sqrt(valor_a, valor_b)  
    
    return render_template("hello.html", result = result)

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")


if __name__ == '__main__':
   app.run()
