import easypost, json
from ep_flask import app, db
from ep_flask.models import Address
easypost.api_key = app.config['EP_API_KEY']

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

def RetrieveAddress(ep_id):
  try:
    address = easypost.Address.retrieve(ep_id)
    res = json.dumps(address.to_dict(), indent=2)
  except easypost.Error as e:
    res = json.dumps(e.json_body, indent=2)
  return res