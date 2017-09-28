"""Karina Ionkina, Ibnul Jahan
SoftDev1 pd7
HW05 -- Jinja Tuning
2017-09-26
"""


from util import helper
#'r' -- read mode: file is only being read.
#file object is created
file = open("data/occupations.csv", 'r')

#initialize empty dictionary
d = helper.csv_to_dict(file)

from flask import Flask, render_template
app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def hello():
    return " <center> <font size = 20px> <a href = '/occupations'> Occupations </a> "

@app.route("/occupations")
def ret():
    title = "Homework 05"
    return  render_template('speed.html', the_title = title, occupation = helper.rand_job(d),  collection = d)
#print d

if __name__=="__main__":
    app.debug = True
    app.run()

