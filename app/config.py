

class Config:
  
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

class ProdConfig(Config):
   
    pass


class DevConfig(Config):
   

    DEBUG =True

# As a user, I would like to see various news sources on the homepage of the application.
# As a user, I would also want to select a news source and see all news articles from the selected news source in the application.
# As a user, I would want to see the image, description and the time a news article was created.
# As a user, I would want to click on an article and read the full article on the source website.    