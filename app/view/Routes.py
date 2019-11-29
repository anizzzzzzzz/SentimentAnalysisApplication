from flask import g, render_template, request

from app import flask_app, SENTIMENT_ANALYZE


@flask_app.route('/')
@flask_app.route('/index')
def index():
    # sent = 'I love this movies.'
    # label,score = SENTIMENT_ANALYZE.classify(sent)
    # print(label,' => ',score)
    # data = {'class_label':label, 'score':score}
    return render_template('index.html')


@flask_app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        review = request.form['review']
        label, score = SENTIMENT_ANALYZE.classify(review)
        # print(label,' => ',score)
        data = {'prediction':label, 'probability':round(score*100, 2), 'content':review}
        return render_template('result.html', data=data)
    else:
        return render_template('index.html')


@flask_app.route('/save-review', methods=['POST', 'GET'])
def save_review():
    if request.method == 'POST':
        review = request.get_json()
        SENTIMENT_ANALYZE.train(review['text'], int(review['prediction']))
        SENTIMENT_ANALYZE.save_sentiment_to_db(review['text'], int(review['prediction']))
        data = {'prediction': '', 'probability': round(0 * 100, 2), 'content': ''}
        return render_template('result.html', data=data)
    else:
        return render_template('error.html')


@flask_app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@flask_app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")