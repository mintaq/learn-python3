from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


@app.route("/")
@make_bold
def hello_world():
    return "Hello world"


@app.route("/<name>")
def greet(name):
    return f"Hello the one and only: {name}!"


if __name__ == "__main__":
    app.run()
