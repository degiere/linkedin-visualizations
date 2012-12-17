import re, nltk, string
from nltk.corpus import stopwords

def tokenize(text):
#    return nltk.word_tokenize(text)
    return nltk.wordpunct_tokenize(text)


def ascii(text):
    return text.encode('ascii', 'replace')


def without_stop_words(tokens):
    return [w for w in tokens if not w in stopwords.words('english')]


def without_punctuation(tokens):
    return [w for w in tokens if not w in string.punctuation]


def without_number_words(tokens):
    return [w for w in tokens if re.findall("^\d*[a-zA-Z][a-zA-Z0-9]*$", w)]


def capitalize_lower(tokens):
    return [w.title() if w.islower() else w for w in tokens]


def normalize(tokens):
    tokens = without_punctuation(tokens)
    tokens = without_stop_words(tokens)
    tokens = without_number_words(tokens)
    tokens = capitalize_lower(tokens)
    return tokens


def vocabulary(tokens):
    return sorted(set(tokens))


def freq_dist(tokens, freq):
    fd = nltk.FreqDist(tokens)
    return sorted([w for w in set(tokens) if fd[w] >= freq])


