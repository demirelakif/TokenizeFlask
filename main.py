from flask import Flask,render_template
from flask_wtf import FlaskForm
from pandas import value_counts
from wtforms.validators import DataRequired
from wtforms import StringField
import os
import Tokenize



class dataForm(FlaskForm):
    name = StringField('data', validators=[DataRequired()])

app = Flask(__name__)
data = []
result = []
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/",methods=['GET', 'POST'])
def index():
    form = dataForm()
    if form.validate_on_submit():
        data.append(form.name.data)
        result.append(Tokenize.start(form.name.data))
        return render_template("index.html",form = form,data=data ,result=result)

    return render_template("index.html",form = form,data=data,result=result)

@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run(debug=True)
