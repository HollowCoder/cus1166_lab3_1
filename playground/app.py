import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

app.config.from_object