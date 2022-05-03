from flask import render_template,request,redirect,url_for
from . import main
from ..request import getNews,getNewsSources



@main.route('/')
def index():

  title = "Welcome to News World"
 
  allSources = getNewsSources()
  
  return render_template('index.html', title = title,sources = allSources)
 

@main.route('/news/<id>')
def news(id):
  title = 'Welcome to News World'

  newsInSource = getNews(id)
  

  return render_template('news.html', title = title, news_list = newsInSource )