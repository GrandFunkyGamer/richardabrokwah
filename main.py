from flask import Flask, render_template, request, redirect

from google.appengine.ext import ndb

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', work_list=WORK)


from data import WORK

