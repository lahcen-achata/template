from flask import Flask           # import flask
from flask import render_template
app = Flask(_name_)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if _name_ == "_main_":        # on running python app.py
    app.run()                     # run the flask app