from ep_flask import db

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ep_address_id = db.Column(db.String(64), index=True, unique=True)

  def __repr__(self):
    return '<ep_address_id:{}>'.format(self.iep_address_idd)    