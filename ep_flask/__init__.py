from flask import Flask
from config import Config
# Flask Bootstrap
from flask_bootstrap import Bootstrap
# SQL Alchemy / Migrate (https://flask-migrate.readthedocs.io/en/latest/)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Moment.js extension (https://blog.miguelgrinberg.com/post/flask-moment-flask-and-jinja2-integration-with-momentjs)
from flask_moment import Moment

# Flask App instance
app = Flask(__name__)
app.config.from_object(Config)

# DB instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import modules
from ep_flask import routes, api, models

# Bootstrap instance
bootstrap = Bootstrap(app)

# Moment extension instance
moment = Moment(app)