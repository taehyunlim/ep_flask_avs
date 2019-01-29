import easypost, json
from ep_flask import app
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
  except easypost.Error as e:
    res = e.json_body
  return res
