from flask import Flask#, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy

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

if __name__ == "__main__":
    app.run(debug=True)