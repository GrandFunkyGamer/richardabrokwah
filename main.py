from google.appengine.ext import ndb
from flask import Flask, render_template, request, redirect
from data import WORK

app = Flask(__name__)


@app.route('/')
def home():
	print(WORK)
	return render_template('index.html', work_list=WORK)