import json

def parse(json_str):
    return json.loads(json_str)


def positions_str(positions):
    s = ""
    for pos in positions:
        s += pos['title'] + ' ' + pos['company']['name'] + ' ' + pos['summary'] + ' '
    return s


def connections_str(connections):
    s = ""
    for c in connections:
        s += c['firstName'] + ' ' + c['lastName'] + ' | '
        s += c['id']
        s += '\n'
    return s


