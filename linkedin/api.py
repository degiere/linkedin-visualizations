import oauth2 as oauth
import config

base_url = "http://api.linkedin.com/v1"

def client():
    cfg = config.config_parser()
    consumer_key = cfg.get('auth', 'consumer_key')
    consumer_secret = cfg.get('auth', 'consumer_secret')
    user_token = cfg.get('auth', 'user_token')
    user_secret = cfg.get('auth', 'user_secret')
    # TODO: only works on profile for developer api user, add real oauth
    consumer = oauth.Consumer(consumer_key, consumer_secret)
    access_token = oauth.Token(user_token, user_secret)
    return oauth.Client(consumer, access_token)


def profile():
    fs = ":(first-name,last-name,positions)"
    url = base_url + "/people/~" + fs + "?format=json"
    resp, content = client().request(url, "GET")
    return content


