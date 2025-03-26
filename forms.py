from flask_wtf import FlaskForm as fm
from wtforms import (
    StringField as stf,
    PasswordField as pf,
    SubmitField as sf,
    validators as vs,
)


class Sign_Up(fm):
    email = stf("E-mail",[
        vs.DataRequired("Please enter an e-mail"),
        vs.Length(min=2, max=25)],
        render_kw={"placeholder": "E-mail"}
        )
    
    first_name = stf("First Name",[
        vs.DataRequired("Please enter a first name"),
        vs.Length(min=2, max=25)],
        render_kw={"placeholder": "First Name"}
        )
    
    last_name = stf("Last Name",[
        vs.DataRequired("Please enter a last name"),
        vs.Length(min=2)],
        render_kw={"placeholder": "Last Name"}
        )
    
    password = pf(
        "Password",[
        vs.InputRequired("Please enter a password"),
        vs.Length(min=4)],
        render_kw={"placeholder": "Password"}
        )
    
    password_confirm = pf(
        "Confirm Password",[
        vs.Length(min=4),
        vs.DataRequired("Please re-enter password to confirm"),
        vs.EqualTo('password',message="Passwords must match")],
        render_kw={"placeholder":"Confirm Password"}
        )
    
    submit = sf("Sign Up")
    
class Log_In(fm):
    
    email = stf("E-mail", [
        vs.DataRequired("Please enter an e-mail"),
        vs.Length(min=2, max=25)],
        render_kw={"placeholder": "E-mail"
        })
    
    password = pf("Password",
        [vs.DataRequired("Please enter a password"),
        vs.Length(min=2,max=25)],
        render_kw={"placeholder": "Password"
        })
    
    submit = sf("Log In")

class Log_Out(fm):
    submit = sf("Log Out")
    
class Header_Buttons(fm):
    pass