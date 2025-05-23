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


    @app.route("/",methods=["GET","POST"])
    def login():
        li = Log_In()
        message = ""
        if li.is_submitted():
            email = li.email.data
            password = li.password.data
             
            if dbm.login_check(email,password) == True:
                session['email'] = email
                full_name = ' '.join(str(name) for name in dbm.get_full_name(email)) 
                return redirect(url_for("main_page",name=full_name))
            else: 
                flash("Login Failed")
        return render_template("login.html",form=li)
        
    
    @app.route("/signup",methods=["GET","POST"])
    def signup():
        su = Sign_Up()
        if su.is_submitted():
            
            email = su.email.data
            first_name = su.first_name.data
            last_name = su.last_name.data
            password = su.password.data
            
            
            if not dbm.check_email(email):
                flash("Email Error")
                return redirect(url_for("signup"))

            if dbm.check_password_name(first_name, last_name,password):
                flash("Password cannot have first name and/or last name")
                return redirect(url_for("signup"))
            
            if not dbm.check_password_uppercase(password):
                flash("Password must have at least one uppercase letter")
                return redirect(url_for("signup"))
            
            if not dbm.check_password_number(password):
                flash("Password must have at least one number")
                return redirect(url_for("signup"))

            if dbm.already_exists(email, first_name, last_name):
                flash("User Already Exists")
                return redirect(url_for("signup"))

            dbm.add_to_table(email,first_name, last_name,password,) # Adds provided data to database table if email string matches regex
            
            full_name = ' '.join(str(name) for name in dbm.get_full_name(email))
            
            return redirect(url_for("main_page",name=full_name))
        return render_template("signup.html", form=su)

    @app.route("/main",methods=["GET","POST"])
    def main_page():
        lo = Log_Out()
        if lo.is_submitted():
            session.pop('email',None)
            return redirect(url_for("login"))
        return render_template("welcome.html",name=request.args.get('name'))
    
    @app.route("/users", methods=["GET"])
    def get_users():
        users_list = dbm.show_table()
        return jsonify(list(users_list)), 200

    @app.route("/user/<user_id>", methods=["GET"])
    def get_user(user_id):
        row = dbm.get_user_by_id(user_id)
        return jsonify(row), 200
    

