import re, nltk
from nltk.corpus import stopwords

def tokenize(text):
    return nltk.regexp_tokenize(text, "[\w]+")


def without_stop_words(text):
    return [w for w in text if not w in stopwords.words('english')]


def without_number_words(text):
    return [w for w in text if re.findall("^\d*[a-zA-Z][a-zA-Z0-9]*$", w)]


def meaning_words(text):
    s = without_stop_words(text)
    s = without_number_words(s)
    return s


def freq_dist(text, freq):
    fdist = nltk.FreqDist(text)
    return sorted([w for w in set(text) if fdist[w] >= freq])
