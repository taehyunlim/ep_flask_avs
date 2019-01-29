import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))

class Config(object):
  # Get secret_key from environment variable or use dummy key
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-secret-key'

  # Flask-SQLAlchemy config
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  # SQLALCHEMY_TRACK_MODIFICATIONS = False

  # EasyPost API Key
  EP_API_KEY = os.environ.get('EP_API_KEY')