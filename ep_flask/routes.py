from flask import render_template, flash, redirect
from ep_flask import app
from ep_flask.forms import AddressForm
from ep_flask.api import CreateAddress

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/address', methods=['GET', 'POST'])
def address():
  form = AddressForm()
  if form.validate_on_submit():
    res = CreateAddress(form)
    flash('EP Address ID: {}'.format(res))
  return render_template('address.html', form=form)