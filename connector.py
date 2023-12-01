import json
from flask import Flask, request, jsonify, redirect, url_for, render_template
from db_manager import db_manager
from forms import Sign_up
from flask_socketio import SocketIO


app = Flask(__name__)
app.config["SECRET_KEY"] = "qwertyuiop"
dbm = db_manager()


# Sample data
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
]


class connector:
    def __init__(self):
        app.run(debug=True, use_reloader=True)
        pass

    @app.route("/get-users")
    def get_users():
        users_list = dbm.show_table()
        return jsonify(list(users_list)), 200

    @app.route("/get-user/<user_id>")
    def get_user(user_id):
        row = dbm.get_user_by_id(user_id)
        return jsonify(row), 200

    @app.route("/create-user", methods=["POST"])
    def create_user():
        user = request.get_json()
        print(user["email"])
        dbm.add_to_table(user["email"], user["name"], user["user_id"])
        return "User Successfully Created", 201

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        su = Sign_up()
        if su.is_submitted():
            result = request.form
            print(su.email.data)
            return render_template("index.html", result=result)
        return render_template("signup.html", form=su)
