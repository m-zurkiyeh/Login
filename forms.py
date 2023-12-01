from flask_wtf import FlaskForm as fm
from wtforms import StringField as stf, PasswordField as pf, SubmitField as sf


class Sign_up(fm):
    first_name = stf("First Name")
    last_name = stf("Last Name")
    email = stf("E-mail")
    password = pf("Password")
    submit = sf("Submit")
