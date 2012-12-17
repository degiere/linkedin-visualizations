import json

def parse(json_str):
    return json.loads(json_str)


def positions_str(positions):
    s = ""
    for pos in positions:
        s += pos['title'] + '\n'
        s += pos['company']['name'] + '\n'
        s += pos['summary'] + '\n'
    return s


def raw(profile):
    return positions_str(positions = profile['positions']['values'])


def connections_str(connections):
    s = ""
    for c in connections:
        s += c['firstName'] + ' ' + c['lastName'] + ' | '
        s += c['id']
        s += '\n'
    return s


