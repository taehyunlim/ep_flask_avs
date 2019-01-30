from ep_flask import db

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ep_adr_id = db.Column(db.String(64), index=True, unique=True)

  def __repr__(self):
    return '<ep_adr_id: {}>'.format(self.ep_adr_id)