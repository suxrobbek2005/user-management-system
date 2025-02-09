import hashlib
from flask import Flask, request, render_template, flash, redirect, url_for
import settings
from db import get_user, enter_infos

app = Flask(__name__)
app.secret_key = getattr(settings, "secret_key", "your_default_secret_key")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        form = request.form

        user = get_user(form.get('username'))
        if user:
            flash("Siz tanlagan username mavjud.")
            return render_template('register.html')

        user = {
            "name": form.get('name'),
            "username": form.get('username'),
            "password": hashlib.sha256(form.get('password', "").encode()).hexdigest()
        }
        enter_infos(user['name'], user['username'], user['password'])

        return redirect(url_for('login'))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        form = request.form
        username = form.get('username')
        password = form.get('password')

        user = get_user(username)
        if user and user['password'] == hashlib.sha256(password.encode()).hexdigest():
            # Foydalanuvchi mavjud va parol to'g'ri
            flash("Muvaffaqiyatli kirish!")
            return redirect(url_for('some_protected_page'))  # Kirish muvaffaqiyatli bo'lsa, boshqa sahifaga yo'naltirish
        else:
            flash("Noto'g'ri foydalanuvchi nomi yoki parol.")
            return render_template('login.html')

    return render_template("login.html")
    
    return "login page"

if __name__ == '__main__':
    app.run(debug=True, port=8000)
