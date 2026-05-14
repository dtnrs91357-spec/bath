from flask import Flask , render_template , request , session , redirect , url_for
from classbox import Login 


app = Flask(__name__)

@app.route("/")
def session():
    if "" not in session:
        return render_template("login.html")
    else:
        return redirect("")
    
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        pswd = request.form.get("password")

    user = Login(name,pswd)
    answer = user.login()

    if answer:
        return render_template("home.html")
    else:
        return render_template("login.html",error="失敗")
    
@app.route("/login_new",methods=["GET","POST"])
def login_new():
    if request.method == "POST":
        name = request.form.get("username")
        pswd = request.form.get("password")

    user = Login(name,pswd)
    answer = user.login_new()

    if answer:
        return render_template("home.html")
    else:
        return render_template("login_new.html",error="失敗")

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8888,debug=True)