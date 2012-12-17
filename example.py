from linkedin import api, parser, text


json_prof = api.profile()
print json_prof

profile = parser.parse(json_prof)
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

json_conn = api.connections()
connections = parser.parse(json_conn)['values']
print parser.connections_str(connections)
