import os
from flask import Flask, render_template
"""
First, we're importing our Flask class
"""

app = Flask(__name__)
"""
We're then creating an instance of this and
storing it in a variable called 'app'
"""

"""
The first argument of the Flask class,
is the name of the application's module - our package.
Since we're just using a single module, we can use __name__
which is a built-in Python variable.
Flask needs this so that it knows
where to look for templates and static files
"""


@app.route("/")
def index():
    return render_template("index.html")


"""
When we try to browse to the root directory,
as indicated by the "/", then Flask triggers
the index function underneath and returns
the "Hello, World" text.
"""

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def about():
    return render_template("contact.html")

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
