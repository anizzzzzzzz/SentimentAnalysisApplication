import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import __root__
from app.Config import Config

ROOT_PATH = __root__.getPath()
template_path = os.path.join(ROOT_PATH, 'templates')
static_path = os.path.join(ROOT_PATH, 'static')

flask_app = Flask(__name__, static_folder=static_path, template_folder=template_path)
flask_app.config.from_object(Config)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from app.service.SGDSentimentAnalysis import SGDSentimentAnalysis

model_path = os.path.join(ROOT_PATH, 'model/sgd_sentiment_analysis.pkl')
stopwords_path = os.path.join(ROOT_PATH, 'model/stopwords.pkl')
# sentiment_analyze = SentimentAnalysis(model_path=model_path)
sentiment_analyze = SGDSentimentAnalysis(model_path=model_path, stopwords_path=stopwords_path)
SENTIMENT_ANALYZE = sentiment_analyze.load_model()

URL = 'http://127.0.0.1:5000/'

from app.model import Sentiment
from app.view import Routes