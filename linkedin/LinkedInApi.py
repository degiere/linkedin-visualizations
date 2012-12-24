import oauth2 as oauth
import config


class LinkedInApi:
    """Linked-in API"""
    base_url = "http://api.linkedin.com/v1"

    def __init__(self, user_token, user_secret):
        self.user_token = user_token
        self.user_secret = user_secret

    def client(self):
        cfg = config.config_parser()
        consumer_key = cfg.get('auth', 'consumer_key')
        consumer_secret = cfg.get('auth', 'consumer_secret')
        consumer = oauth.Consumer(consumer_key, consumer_secret)
        token = oauth.Token(key=self.user_token,secret=self.user_secret)
        return oauth.Client(consumer, token)

    def profile(self):
        fs = ":(first-name,last-name,positions)"
        url = LinkedInApi.base_url + "/people/~" + fs + "?format=json"
        resp, content = self.client().request(url, "GET")
        return content

    def connections(self):
        url = LinkedInApi.base_url + "/people/~/connections?format=json"
        resp, content = self.client().request(url, "GET")
        return content

