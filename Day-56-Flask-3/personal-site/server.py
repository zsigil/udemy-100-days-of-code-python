from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/<name>')
def hello(name=None):
    return render_template('josh.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
