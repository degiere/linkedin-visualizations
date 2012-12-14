import json

def parse(json_str):
    return json.loads(json_str)


def positions_str(positions):
    s = ""
    for pos in positions:
        s += pos['title'] + ' '
        s += pos['company']['name'] + ' '
        s += pos['summary'] + ' '
    return s
