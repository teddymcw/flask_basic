from flask.ext.wtf import Form 
from wtforms import StringField, SubmitField #TextField, 
from wtforms.validators import DataRequired, Length

class BasicForm(Form):
    basic_form = StringField("the_basic_form")#, validators=[DataRequired()])

class InputForm(Form):
    x_or_o = StringField(u'x-or-o', validators=[DataRequired(), \
        Length(min=0, max=2, message="input must be 'x' or 'o'")])
    submit = SubmitField('Submit')

