from linkedin import api, parser, nlp
import nltk

json = api.profile()
#print json_prof

profile = parser.parse(json)
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
