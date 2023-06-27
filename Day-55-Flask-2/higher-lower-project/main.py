from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1><img style='width:300' src='https://media1.giphy.com/media/3ohjURGyi3xk5x8H6M/200.webp?cid=ecf05e475r6ets7l8i1gamtm6wf79fp0rglf9hmaejbe997j&ep=v1_gifs_search&rid=200.webp&ct=g'>"


@app.route('/<number>')
def numberpage(number):
    if int(number) == random_number:
        return "<h1>You got it!</h1><img style='width:300' src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif int(number) < random_number:
        return "<h1>Too low. Try again.</h1><img style='width:300' src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1>Too high. Try again.</h1><img style='width:300' src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
