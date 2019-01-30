from ep_flask import db
from datetime import datetime

class Address(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ep_adr_id = db.Column(db.String(64), index=True, unique=True)
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __repr__(self):
    return '<ep_adr_id: {} @{}>'.format(self.ep_adr_id, self.timestamp)