from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourOwFour(error):
  return render_template('fourOwFour.html'),404