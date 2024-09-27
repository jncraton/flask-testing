from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """Hello, world! <a href="/add">Add</a>"""

@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"The sum is {a+b}" 
