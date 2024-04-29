from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style = 'color:green'>Hello World</h1> <h2>this is good</h2>"


app.run(debug=True)
