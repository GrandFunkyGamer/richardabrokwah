from google.appengine.ext import ndb
from flask import Flask, render_template, request, redirect
from data import WORK
from data import BLOG

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html', work_list=WORK, blog_list=BLOG)