import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")


def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 5000)),
        debug=True)

"""
We should never have "debug=True" in a production application,
or when we submit our projects for assessment.
This is very important, because having debug=True
can allow arbitrary code to be run, this is a security flaw.
You should only have debug=True while testing your
application in development mode, but change it to
debug=False before you submit your project
"""
