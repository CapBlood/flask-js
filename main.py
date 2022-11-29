import os

from flask import Flask, render_template

app = Flask(__name__)
app._static_folder = os.path.abspath("static/")


@app.route("/")
def hello_world():
    return render_template('main.html')


if __name__ == "__main__":
    app.run()
