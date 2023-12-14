from flask_wtf import FlaskForm as fm
from wtforms import (
    StringField as stf,
    PasswordField as pf,
    SubmitField as sf,
    validators as vs,
)


class Sign_up(fm):
    email = stf("E-mail", [vs.DataRequired("Please enter an e-mail"),vs.Length(min=4, max=25)])
    first_name = stf("First Name", [vs.DataRequired("Please enter a first name"),vs.Length(min=4, max=25)])
    last_name = stf("Last Name", [vs.DataRequired("Please enter a last name"),vs.Length(min=4, max=25)])
    password = pf("Password",[vs.DataRequired("Please enter a password")])
    submit = sf("Submit")
