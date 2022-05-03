from flask import Flask
from flask import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):

  app = Flask(__name__)

  #setup of configurations
  app.config.from_object(config_options[config_name])

  #initializing extensions
  bootstrap.init_app(app)

  return app



