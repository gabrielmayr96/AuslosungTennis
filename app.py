from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    teams = []
    if request.method == "POST":
        names = request.form.get("names").splitlines()
        random.shuffle(names)
        teams = [names[i:i+2] for i in range(0, len(names), 2)]
    return render_template("index.html", teams=teams)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
