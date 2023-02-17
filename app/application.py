from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.app_context().push()

from teapot.teapot_class import Teapot
teapot = Teapot()
import views, models

from teapot.teapot_actions import insert_initial_data
insert_initial_data()
