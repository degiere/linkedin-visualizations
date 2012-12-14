import oauth2 as oauth
import os
from ConfigParser import SafeConfigParser

base_url = "http://api.linkedin.com/v1"

def client():
    config = config_parser()
    consumer_key = config.get('auth', 'consumer_key')
    consumer_secret = config.get('auth', 'consumer_secret')
    user_token = config.get('auth', 'user_token')
    user_secret = config.get('auth', 'user_secret')
    # TODO: only works on profile for developer api user, add real oauth
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    access_token = oauth.Token(user_token, user_secret)
    return oauth.Client(consumer, access_token)


def profile():
    fs = ":(first-name,last-name,positions)"
    url = base_url + "/people/~" + fs + "?format=json"
    resp, content = client().request(url, "GET")
    return content


def config_parser():
    parser = SafeConfigParser()
    parser.read('default.cfg')
    # copy the above here and set app credentials
    parser.read(os.path.expanduser('~/.linkedin.cfg'))
    return parser
