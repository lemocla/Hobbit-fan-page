import os
from flask import Flask, render_template


app = Flask(__name__)
# in Flask, the convention is that our variable is called 'app'.
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__" :
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), # "5000" common port used by flast
        debug = True
    )




