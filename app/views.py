from flask import render_template
from app import app
from .request import getNews


@app.route('/')
def index():

  title = "Welcome to News World"

  current_sports = getNews('sports')
  current_health = getNews('health')
  current_entertainment = getNews('entertainment')
  current_technology = getNews('technology')


  return render_template('index.html', title = title,sports = current_sports,
  health = current_health, entertainment = current_entertainment,
  technology = current_technology)