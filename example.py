from linkedin import LinkedInApi, parser, nlp
import nltk
from tokens import user_token, user_secret


api = LinkedInApi.LinkedInApi(user_token, user_secret)


def doIt():
    json_prof = api.profile()
    print json_prof

    profile = parser.parse(json_prof)
    #print "Name: " + profile['firstName'] + ' ' + profile['lastName']
    raw = parser.raw(profile)
    raw = nlp.ascii(raw)

    tokens = nlp.tokenize(raw)
    tokens = nlp.normalize(tokens)
    print "Tokens:"
    print ' '.join(tokens)

    freq = nlp.freq_dist(tokens, 3)
    print "Frequent:"
    print ' '.join(freq)

    vocab = nlp.vocabulary(tokens)
    print "Vocabulary: "
    print vocab

    text = nltk.Text(tokens)
    print "Text: " + str(type(text))


    #json_conn = api.connections()
    #connections = parser.parse(json_conn)['values']
    #print parser.connections_str(connections)

def peopleSearch():
    results = api.peopleSearch("java%20spring%20cassandra")
    print parser.parse(results)

if __name__ == "__main__":
    peopleSearch()
    #doIt()