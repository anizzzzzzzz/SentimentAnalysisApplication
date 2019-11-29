import re

def preprocessor(text):
    text = re.sub(r'<[^>]*>', '', text)
    emoticons = re.findall(r'(?::|;|=)?(?:-)?(?:\(|\)|D|P)', text)
    text = re.sub(r'[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-','')
    return text

def tokenizer(text):
    return text.split()

def porter_tokenizer(stemmer, text):
    return [stemmer.stem(w) for w in text.split()]

def remove_stop_words(stopwords, text):
    return [w for w in text.split() if w not in stopwords]
