import json
from flask import (
    Flask,
    request,
    jsonify,
    redirect,
    url_for,
    render_template,
    flash,
)
from db_manager import db_manager
from forms import Sign_up


app = Flask(__name__)
app.config["SECRET_KEY"] = "qwertyuiop"
dbm = db_manager()


class connector:
    def __init__(self):
        """
        Runs the flask application on call

        Keyword arguments:
        self -- the class's own instance

        """

        app.run(debug=True, use_reloader=True)

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
        dbm.add_to_table(user["email"], user["fname"], user["lname"], user["password"])
        return "User Successfully Created", 201

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        su = Sign_up()
        message = ""
        if su.is_submitted():
            result = request.form
            if not dbm.check_email(su.email.data):
                flash("Email Error")
                return redirect(url_for("signup"))

            if dbm.check_if_already_exists(
                su.email.data, su.first_name.data, su.last_name.data
            ):
                flash("User Already Exists")
                return redirect(url_for("signup"))

            dbm.add_to_table(su.email.data,su.first_name.data, su.last_name.data,su.password.data,) # Adds provided data to database table if email string matches regex
            flash("Successfully Created User")
            return redirect(url_for("signup"))
        return render_template("signup.html", form=su)

    @app.route("/")
    def index():
        """ 
        the API's home page

        Returns:
            str: render_template("index.html")
        
        """
        return render_template("index.html")
