from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from pandas import value_counts
from wtforms.validators import DataRequired
from wtforms import StringField
import os
import Tokenize
import csv
import pandas as pd


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
# if __name__ == "__main__":
#     # app.run(debug=True)


@app.route("/VeriEkle",methods=["GET","POST"])
def VeriEkle():
    if request.method=="POST":
        key = request.form.get('urun')
        tag = request.form.get('tag_select')
        category = request.form.get('category_select')
        description = request.form.get('description')

        line_no = check_csv(key)
        if line_no:
            write_csv(key,tag,category,description,line_no)
        return render_template("VeriEkle.html")

    return render_template("VeriEkle.html")
    



def write_csv(key,tag,category,description,line_no):
    df = pd.DataFrame({'Id': [line_no],
                   'Key': [key],
                   'Tag': [tag],
                   'Category': [category],
                   'Description': [description],
                   })


    df.to_csv('test.csv', mode='a', index=False, header=False)



def check_csv(data):
    with open('test.csv',encoding="UTF-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1

            else:
                if row[1] == data:
                    return False
                    
                line_count += 1
        return line_count



if __name__ == "__main__":
    app.run(debug=True)
