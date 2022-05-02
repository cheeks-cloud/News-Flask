from app import app
import urllib.request,json
from .models import news

News = news.News
apiKey = None
base_url = None 

apiKey = app.config['NEWS_API_KEY']
base_url  = app.config["NEWS_API_BASE_URL"]


def getNews(category):

  getNews_url = base_url.format(category,apiKey)

  with urllib.request.urlopen(getNews_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['articles']:
      news_results_list = get_news_response['articles']
      news_results = process_results(news_results_list)

  return news_results




def getNewsDetails(id):
  get_news_details_url = base_url.format(id,apiKey)

  with urllib.request.urlopen(get_news_details_url)as url:
    news_details_data = url.read()
    news_details_response = json.loads(news_details_data)

    news_object = None
    if news_details_response:
      id = news_details_response.get('id')
      name = news_details_response.get('name')
      title = news_details_response.get('title')
      image =news_details_response.get('urlToImage')
      description = news_details_response.get('description')
      author = news_details_response.get('author')

      news_object = News(id,name,title,description,author,image)

    return news_object


def process_results(news_list):
  news_results = []
  for news_item in news_list:
    id = news_item.get('id')
    name = news_item.get('name')
    title = news_item.get('title')
    image = news_item.get('urlToImage')
    description = news_item.get('description')
    author = news_item.get('author')

    if image:
      news_object = News(id,name,title,image,description,author)
      news_results.append(news_object)

  return news_results


 