
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/portfolio")
def portfolio():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()
