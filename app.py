from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from ics import Calendar
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'supersecretkey'
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ics_url = request.form["ics_url"]
        return redirect(url_for("events", ics_url=ics_url))
    return render_template("home.html")


@app.route("/events")
@login_required
def events():
    ics_url = request.args.get("ics_url")
    
    if not ics_url:
        return redirect(url_for("home"))

    try:
        response = requests.get(ics_url)
        if response.status_code != 200:
            return render_template("events.html", events=[], error="Nie udało się pobrać kalendarza.")

        calendar = Calendar(response.text)
        future_events = sorted(
            (event for event in calendar.events if event.begin.datetime >= datetime.now(timezone.utc)),
            key=lambda e: e.begin
        )

        return render_template("events.html", events=future_events[:10], error=None)

    except Exception as e:
        return render_template("events.html", events=[], error=str(e))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Użytkownik już istnieje")
            return redirect(url_for("register"))

        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Niepoprawne dane logowania!")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("home"))
    return render_template("login.html")    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
