from flask import render_template
from app import app

@app.errorhandler(404)
def fourOwFour(error):
  return render_template('fourOwFour.html'),404