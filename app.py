
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("intr.html")

@app.route("/portfolio")
def portfolio():
    return render_template("inde.html")

if __name__ == "__main__":
    app.run()
