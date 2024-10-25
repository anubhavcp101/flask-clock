from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/oldhome" )
def oldhome():
    return "This is the Old home page <h1>Home</h1>"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello Buddy, {name}"

a = False
@app.route("/admin")
def admin():
    if a:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("user",name="Admin"))
    
@app.route("/login", methods=["POST","GET"])    
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", name=user))
    else:
        return render_template("login.html")
    
@app.route("/anaclock")
def anaClock():
    return render_template("ana-clock.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)