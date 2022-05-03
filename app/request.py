from app import app
import urllib.request,json
from .models import news

News = news.News
NewSource = news.NewSource
apiKey = None
base_url = None 

apiKey = app.config['NEWS_API_KEY']
base_url  = app.config["NEWS_API_BASE_URL"]
bases_url = app.config["NEWS_SOURCES_BASE_URL"]


def getNews(sources):

  getNews_url = base_url.format(sources,apiKey)

  with urllib.request.urlopen(getNews_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_results = None

    if get_news_response['articles']:
      news_results_list = get_news_response['articles']
      news_results = process_results(news_results_list)

  return news_results

def getNewsSources():
  get_news_sources_url = bases_url.format(apiKey)
     
  with urllib.request.urlopen(get_news_sources_url) as url:
    news_sources_data = url.read()
    news_sources_response = json.loads(news_sources_data)

    sources_object = None
    
    if news_sources_response['sources']:
      news_sources_list = news_sources_response['sources']
      sources_object = process_sources(news_sources_list)
 
  return sources_object


def process_results(news_list):
  news_results = []
  for news_item in news_list:
    id = news_item.get('id')
    name = news_item.get('name')
    title = news_item.get('title')
    image = news_item.get('urlToImage')
    description = news_item.get('description')
    author = news_item.get('author')
    date = news_item.get('publishedAt')

    if image:
      news_object = News(id,name,title,image,description,author,date)
      news_results.append(news_object)

  return news_results

def process_sources(sources):
  allSources = []
  for source in sources:
    name = source.get('name')
    description = source.get('description')
    language = source.get('language')
    country = source.get('country')

    oneSource = NewSource(name, description, language, country)
    allSources.append(oneSource)

  return allSources







 