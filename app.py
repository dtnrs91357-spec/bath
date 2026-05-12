from flask import Flask , render_template , request , session , redirect , url_for
import mysql.connector
from fund import db_connect

app = Flask(__name__)

@app.route("/")
def session():
    if "" not in session:
        return render_template("login.html")
    else:
        return redirect("")

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8888,debug=True)