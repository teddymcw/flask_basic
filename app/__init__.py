from flask import Flask, render_template, flash, request
from flask.ext.sqlalchemy import SQLAlchemy
from forms import BasicForm, InputForm

#for config
import os

#instantiations needed
app = Flask(__name__)
db = SQLAlchemy(app)

#make shift config section
#    below is for CSFR prevention by wtforms
app.config['SECRET_KEY'] = 'something'
#find this file
basedir = os.path.abspath(os.path.dirname(__file__))
#db section
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


@app.route("/")
def hello():
    return "test success!!!"


@app.route("/basic_form", methods=["GET", "POST"])
def basic_form():
    form = BasicForm()
    if form:
        flash("you are validated")
        data = form.basic_form.data
        print(data)
        print 'valid test'
    else:
        flash("ehhh...ehh!, form didn't go")
        print 'invalid test'
    return render_template("basic_form.html", form=form)

#util function for ttt
def print_board():   
    return board[:3], board[3:6], board[6:9]

#test application code for db, forms and such
board = [str(num) for num in range(10)]
@app.route("/play", methods=["GET", "POST"])
def show_board():
    new_board = print_board()
    form=InputForm()
    print "test"
    if form.validate_on_submit():
        flash("you are validated")
        print 'valid test'
    else:
        flash("ehhh...ehh!, form didn't go")
        print 'invalid test'
    return render_template("test.html", form=form, board_1=new_board[0], \
                                                    board_2=new_board[1], \
                                                    board_3=new_board[2])
  
#route to display some of flasks features
@app.route("/fun")
def fun():
    user_agent = request.headers.get('User-Agent')
    print(dir(request.headers))
    return '<p>Your browser is %s</p>' % user_agent



if __name__ == "__main__":
    app.run(debug=True)