from flask.ext.wtf import Form 
from wtforms import TextField
from wtforms.validators import DataRequired, Length

class InputForm(Form):
    x_or_o = TextField(u'x-or-o', validators=[DataRequired(), \
        Length(min=1, max=1, message="input must be 'x' or 'o'")])