import hashlib
from flask import Flask, request, render_template, flash, redirect, url_for
import settings
from db import get_user, enter_infos


app = Flask(__name__)
app.secret_key = settings.secret_key


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form = request.form

        user = get_user(form['username'])
        if user:
            flash("Siz tanlagan username mavjud.")
            return render_template('register.html')

        user = {
            "name": form['name'],
            "username": form['username'],
            "password": hashlib.sha256(form['password'].encode()).hexdigest()
        }
        enter_infos(user['name'], user['username'], user['password'])

        return redirect(url_for('login'))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return "login page"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
