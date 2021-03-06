from flask import render_template, flash, redirect, request, url_for, jsonify, session
from ep_flask import app, db
from ep_flask.forms import AddressForm
from ep_flask.api import CreateAddress, RetrieveAddress, CreateAddressForceUpdate, CreateAddressEditModal
from ep_flask.models import Address

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
  return redirect(url_for('address_1'))

@app.route('/address', methods=['GET', 'POST'])
def address():
  form = AddressForm()
  if form.validate_on_submit():
    res = CreateAddress(form)
    return render_template('address.html', form=form, res=res)
  return render_template('address.html', form=form)

@app.route('/address_1', methods=['GET', 'POST'])
def address_1():
  key = session.get('key')
  form = AddressForm()
  if form.validate_on_submit():
    (input, res, output) = CreateAddressForceUpdate(form, key)
    return render_template('address_1.html', form=form, input=input, res=res, output=output)
  return render_template('address_1.html', form=form)

@app.route('/address_2', methods=['GET', 'POST'])
def address_2():
  form = AddressForm()
  return render_template('address_2.html', form=form)

@app.route('/avs', methods=['POST'])
def avs():
    key = session.get('key')
    (input, res, output) = CreateAddressEditModal(request.form, key)
    result = {
      'input': input,
      'res': res,
      'output': output
    }
    return jsonify(result)

@app.route('/store_key', methods=['POST'])
def save_api_key():
  key = request.form['key']
  print(key)
  session['key'] = key
  return key

@app.route('/get_key', methods=['GET'])
def get_api_key():
    key = session.get('key') or ''
    return key

@app.route('/address/<id>/retrieve', methods=['GET'])
def retrieve_address(id):
  res = RetrieveAddress(id)
  return res

@app.route('/address/<id>/delete', methods=['GET', 'DELETE'])
def delete_address(id):
  address = Address.query.filter_by(id=id).first()
  db.session.delete(address)
  db.session.commit()
  return redirect(url_for('index'))