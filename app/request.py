from app import app
import urllib.request,json
from .models import news

News = news.News 

apiKey = app.config['NEWS_API_KEY']
base_url  = app.config['NEWS_API_BASE_URL']


def getNews(category):

  getNews_url  = base_url.format(category,apiKey)

  with urllib.request.urlopen(getNews_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['results']:
      news_results_list = get_news_response['results']
      news_results = process_results(news_results_list)

  return news_results


# def process_results(news_list):
#   news_results = []
#   for news_item in news_list:
#     name = news_item.get('name')
#     title = news_item.get('title')
#     image = news_item.get('urlToImage')
#     description = news_item.get('description')
#     author = news_item.get('author')

#     if image:
#       news_object = News()


 