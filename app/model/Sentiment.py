from datetime import datetime

from app import db


class Sentiment(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    review = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Integer, nullable=False)
    createdDate = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return 'Review (sentiment = %d, review=%s )' % (self.sentiment, self.review)

    def __init__(self, review, sentiment):
        self.review = review
        self.sentiment = sentiment

