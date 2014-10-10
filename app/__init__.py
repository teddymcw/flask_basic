from flask import Flask, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from forms import InputForm

#for config
import os

#instantiations needed
app = Flask(__name__)
db = SQLAlchemy(app)

#make shift config section
#    below is for CSFR prevention by wtforms
app.config['SECRET_KEY'] = 'hard to guess string'
#find this file
basedir = os.path.abspath(os.path.dirname(__file__))
#db section
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


@app.route("/")
def hello():
    return "test success!!!"

def print_board():   
    return board[:3], board[3:6], board[6:9]

#test application code for db, forms and such
board = [str(num) for num in range(10)]
@app.route("/play", methods=["GET", "POST"])
def show_board():
    new_board = print_board()
    form=InputForm()
    if form.validate_on_submit():
        flash("you are validated")
    else:
        flash("ehhh...ehh!, form didn't go")
    return render_template("test.html", form=form, board_1=new_board[0], \
                                                    board_2=new_board[1], \
                                                    board_3=new_board[2])


if __name__ == "__main__":
    app.run(debug=True)