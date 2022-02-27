from flask import Flask, render_template,redirect, url_for, request

user = ' '
second_name = ' '
email = ' '
passwd = ' '

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")\

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registration", methods=["POST", "GET"])
def registration():
    global user
    global second_name
    global email
    global passwd
    if request.method == "POST":
        user = request.form["nm"]
        second_name = request.form["snm"]
        email = request.form["email"]
        passwd = request.form["pswd"]
        return f"Имя:{user}, Фамилия:{second_name}, Емайл:{email}, Пароль:{passwd}"
    else:
        return render_template("registration.html")


if __name__ == "__main__":
    app.run(debug=True)
