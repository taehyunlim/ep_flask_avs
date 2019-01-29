from flask import render_template, flash, redirect
from ep_flask import app

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/address', methods=['GET', 'POST'])
def address():
  return render_template('address.html')