from flask import Flask

from teapot.teapot_class import Teapot

app = Flask(__name__)
teapot = Teapot()
import views
