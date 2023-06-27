from flask import Flask

app = Flask(__name__)


def make_bold(my_func):
    def wrapper_func(*args, **kwargs):
        my_func()
    return wrapper_func


def make_emph(my_func):
    def wrapper_func(*args, **kwargs):
        my_func()
    return wrapper_func


@app.route("/")
def index():
    return "<h1 style='text-align:center'>Index page</h1><p>This is a paragraph</p><img style='width:300px' src='https://media4.giphy.com/media/3GRwYzxwdceaI/200w.webp?cid=ecf05e47j8kthqp1lwf8svo1flbpt9b8zf1g7uhultzzikvp&ep=v1_gifs_search&rid=200w.webp&ct=g'>"


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_emph
def bye():
    return "Bye"


@app.route("/user/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
