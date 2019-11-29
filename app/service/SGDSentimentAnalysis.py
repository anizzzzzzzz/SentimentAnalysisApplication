import pickle
import re
import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer

from app import db
from app.model.Sentiment import Sentiment


class SGDSentimentAnalysis(object):
    def __init__(self, model_path=None, stopwords_path=None):
        self.model_path = model_path
        self.stopwords_path = stopwords_path
        self.label = {0: 'negative', 1:'positive'}

    def load_model(self):
        self.stopwords = pickle.load(open(self.stopwords_path, 'rb'))
        self.vectorizer_ = HashingVectorizer(decode_error='ignore', n_features=2**21, preprocessor=None, tokenizer=self.sgd_preprocessor)
        self.clf = pickle.load(open(self.model_path, 'rb'))
        return self

    def classify(self, document):
        document_vector_ = self.vectorizer_.transform([document])
        y = self.clf.predict(document_vector_)
        proba = np.max(self.clf._predict_proba(document_vector_))
        return self.label[y[0]], proba

    def sgd_preprocessor(self, text):
        text = re.sub(r'<[^>]*>', '', text)
        emoticons = re.findall(r'(?::|;|=)?(?:-)?(?:\(|\)|D|P)', text)
        text = re.sub(r'[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
        tokenized = [w for w in text.split() if w not in self.stopwords]
        return tokenized

    def train(self, document, y):
        X = self.vectorizer_.transform([document])
        self.clf.partial_fit(X, [y])

    def dump_classifier_to_file(self):
        pickle.dump(self.clf, open(self.model_path, 'wb'), protocol=4)

    def save_sentiment_to_db(self, document, y):
        sentiment = Sentiment(review=document, sentiment=y)
        db.session.add(sentiment)
        db.session.commit()
