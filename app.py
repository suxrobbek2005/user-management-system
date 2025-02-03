import hashlib
from flask import Flask, request, render_template, flash
from mysql import connector


app = Flask(__name__)
app.secret_key = "secretkey"



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        form = request.form

        users = list(filter(lambda user: form['username'] == user['username'], users_list))
        if users:
            flash("Siz tanlagan username mavjud.")
            return render_template('register.html')

        user = {
            "name": form['name'],
            "username": form['username'],
            "password": hashlib.sha256(form['password'].encode()).hexdigest()
        }
        users_list.append(user)

        print(users_list)

    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
