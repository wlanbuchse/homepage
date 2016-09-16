# coding: utf8

# Author: Johannes Pawelczyk
# (c) 2016 by Johannes Pawelczyk. All rights reserved.

from flask import Flask, render_template, url_for, request, redirect
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config['SECRET_KEY'] = '9J3a7aNfymT3aXoUZAXJ7QTYDqc2f379'

app.wsgi_app = ProxyFix(app.wsgi_app)

# Routing

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/archiv')
def archiv():
	return render_template('archiv.html')

@app.route('/impressum')
def impressum():
	return render_template('impressum.html')

# Open in debug mode if called directly

if __name__ == '__main__':
	app.debug = True
	app.run(host = 'localhost', port = 5000)