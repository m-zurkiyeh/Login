import json
from flask import (
    Flask,
    session,
    request,
    jsonify,
    redirect,
    url_for,
    render_template,
    flash,
)
from db_manager import db_manager
from forms import *


app = Flask(__name__)       
app.config["SECRET_KEY"] = "Lz8UhFZZK4tIkg53W0JPeKhmubJV7Idz0IBRVsHZaIg3JaFjPh"
dbm = db_manager()


class connector:
    def __init__(self):
        """
        Runs the flask application on call

        Keyword arguments:
        self -- the class's own instance

        """
        app.run(debug=True, use_reloader=True)
        session.clear()


    @app.route("/",methods=["GET","POST"])
    def login():
        li = Log_In()
        message = ""
        if li.is_submitted(): 
            if dbm.exists(li.email.data,li.password.data) == True:
                session['email'] = li.email.data
                user_first_name = dbm.get_first_name(li.email.data)
                return redirect(url_for("main_page",name=user_first_name))
            else: 
                flash("Login Failed")
        return render_template("login.html",form=li)
        
    
    @app.route("/signup",methods=["GET","POST"])
    def signup():
        su = Sign_Up()
        message = ""
        if su.is_submitted():
            if not dbm.check_email(su.email.data):
                flash("Email Error")
                return redirect(url_for("signup"))

            if dbm.check_password_name(su.first_name.data, su.last_name.data,su.password.data):
                flash("Password cannot have first name and/or last name")
                return redirect(url_for("signup"))
            
            if not dbm.check_password_uppercase(su.password.data):
                flash("Password must have at least one uppercase letter")
                return redirect(url_for("signup"))
            
            if not dbm.check_password_number(su.password.data):
                flash("Password must have at least one number")
                return redirect(url_for("signup"))

            if dbm.already_exists(su.email.data, su.first_name.data, su.last_name.data):
                flash("User Already Exists")
                return redirect(url_for("signup"))

    
            
            dbm.add_to_table(su.email.data,su.first_name.data, su.last_name.data,su.password.data,) # Adds provided data to database table if email string matches regex
            flash(f"Welcome {su.first_name.data} {su.last_name.data}!")
            
            return redirect(url_for("signup"))
        return render_template("signup.html", form=su)

    @app.route("/main",methods=["GET","POST"])
    def main_page():
        lo = Log_Out()
        if lo.is_submitted():
            session.pop('email',None)
            return redirect(url_for("login"))
        return render_template("main.html",name=request.args.get('name'))
    
    @app.route("/users", methods=["GET"])
    def get_users():
        users_list = dbm.show_table()
        return jsonify(list(users_list)), 200

    @app.route("/user/<user_id>", methods=["GET"])
    def get_user(user_id):
        row = dbm.get_user_by_id(user_id)
        return jsonify(row), 200
    
    @app.route("/change-user/<user_id>",methods=["PUT"])
    def change_user_page(): 
        pass
        return render_template("index.html")

