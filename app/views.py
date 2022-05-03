from flask import render_template
from app import app
from .request import getNews,getNewsSources



@app.route('/')
def index():

  title = "Welcome to News World"
 
  allSources = getNewsSources()
  
  return render_template('index.html', title = title,sources = allSources)
 

@app.route('/news/<id>')
def news(id):
  title = 'Welcome to News World'

  newsInSource = getNews(id)
  

  return render_template('news.html', title = title, news_list = newsInSource )