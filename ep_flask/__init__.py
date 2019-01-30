from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

# Import modules
from ep_flask import routes, api

# Bootstrap instance
bootstrap = Bootstrap(app)