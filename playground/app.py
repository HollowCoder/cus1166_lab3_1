import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from playground.models import *
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)