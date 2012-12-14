from linkedin import api, parser, text

json = api.profile()
print json

profile = parser.parse(json)
print "Name: " + profile['firstName'] + ' ' + profile['lastName']

positions = profile['positions']['values']

positions_str = parser.positions_str(positions)
tokens = text.tokenize(positions_str)
tokens = text.meaning_words(tokens)
print "Tokens:"
print ' '.join(tokens)

freq = text.freq_dist(tokens, 3)
print "Frequent:"
print ' '.join(freq)