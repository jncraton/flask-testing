from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """Hello, world! <a href="/add">Add</a>"""

@app.route("/add")
def add():
    page = """
    <form action=/add method=get>
        <input name=a />
        <input name=b />
        <input type=submit />
    </form> 
    """

    try:
        a = int(request.args["a"])
        b = int(request.args["b"])
        page += f"<p>The sum is {a+b}</p>"
    except:
        pass

    return page
