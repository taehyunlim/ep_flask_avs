import easypost, json
from ep_flask import app, db
from ep_flask.models import Address
easypost.api_key = app.config['EP_API_KEY']

class AddressData(object):
  name=""
  street1=""
  street2=""
  city=""
  state=""
  zip=""
  country=""
  verify=[]
  ep_id=""

def CreateAddress(form):
  try:
    address = easypost.Address.create(
      verify=[form.verify.data],
      name=form.name.data,
      street1=form.street1.data,
      street2=form.street2.data,
      city=form.city.data,
      state=form.state.data,
      zip=form.zip.data,
      country=form.country.data
    );
    res = address
    db.session.add(Address(ep_adr_id=res.id))
    db.session.commit()
  except easypost.Error as e:
    res = json.dumps(e.json_body, indent=2)
  return res

def CreateAddressForceUpdate(form):
  input = {}
  output = {}
  # form input
  data=AddressData()
  data.name=form.name.data
  data.street1=form.street1.data
  data.street2=form.street2.data
  data.city=form.city.data
  data.state=form.state.data
  data.zip=form.zip.data
  data.country=form.country.data
  input = json.dumps(data.__dict__, indent=2)
  print(input)
  # API
  try:
    res = easypost.Address.create(
      verify=[form.verify.data],
      name=form.name.data,
      street1=form.street1.data,
      street2=form.street2.data,
      city=form.city.data,
      state=form.state.data,
      zip=form.zip.data,
      country=form.country.data
    )
    # Store response in output 
    data = AddressData()
    data.ep_id=res.id
    data.name=res.name
    data.street1=res.street1
    data.street2=res.street2
    data.city=res.city
    data.state=res.state
    data.zip=res.zip
    data.country=res.country
    # Validate address based on delivery or zip4 attribute
    if hasattr(res.verifications, "delivery"):
      if res.verifications.delivery.success:
        output = json.dumps(data.__dict__, indent=2)
      else:
        output = res.verifications.delivery.errors
    elif hasattr(res.verifications, "zip4"):
      if res.verifications.zip4.success:
        output = json.dumps(data.__dict__, indent=2)
      else:
        output = res.verifications.zip4.errors
    print(output)
    # db.session.add(Address(ep_adr_id=res.id))
    # db.session.commit()
  except easypost.Error as e:
    res = json.dumps(e.json_body)
  return input, res, output


def CreateAddressEditModal(form):
  input = {}
  output = {}
  # form input
  data=AddressData()
  data.name=form['name']
  data.street1=form['street1']
  data.street2=form['street2']
  data.city=form['city']
  data.state=form['state']
  data.zip=form['zip']
  data.country=form['country']
  data.verify=form['verify']
  input = data.__dict__
  print(input)
  # API
  try:
    _res = easypost.Address.create(
      verify=[form['verify']],
      name=form['name'],
      street1=form['street1'],
      street2=form['street2'],
      city=form['city'],
      state=form['state'],
      zip=form['zip'],
      country=form['country']
    );
    res = json.loads(_res.to_json())
    print(res)
    # Store response in output 
    data = AddressData()
    # data.ep_id=_res.id
    data.name=_res.name
    data.street1=_res.street1
    data.street2=_res.street2
    data.city=_res.city
    data.state=_res.state
    data.zip=_res.zip
    data.country=_res.country
    data.verify=form['verify']
    output = data.__dict__
    print(output)
    # db.session.add(Address(ep_adr_id=_res.id))
    # db.session.commit()
  except easypost.Error as e:
    res = json.dumps(e.json_body)
  return input, res, output
  

def RetrieveAddress(ep_id):
  try:
    address = easypost.Address.retrieve(ep_id)
    res = json.dumps(address.to_dict(), indent=2)
  except easypost.Error as e:
    res = json.dumps(e.json_body, indent=2)
  return res