from linkedin import config, LinkedInApi, parser, nlp
from flask import Flask, render_template, request, session
from flask.ext.assets import Environment, Bundle
import oauth2
import urllib
import urlparse
import json

app = Flask(__name__)
app.secret_key = 'A0Zr98212asd3yasdf21WX/,?RT'
assets = Environment(app)

jsD3 = Bundle('js/d3.v2.js', 'js/d3.layout.cloud.js', output='gen/packed.js')
assets.register('js_d3', jsD3)
cfg = config.config_parser()


@app.route("/")
def index():
    consumer_key = cfg.get('auth', 'consumer_key')
    return render_template('index.html', key=consumer_key)


@app.route("/token-exchange", methods=['POST'])
def token_exchange():
    oauth_token = None
    oauth_secret = None

    if session.get('linkedin_oauth_token2'):
        print "SESSION"
        oauth_token = session.get('linkedin_oauth_token')
        oauth_secret = session.get('linkedin_oauth_secret')
        access_token = oauth_token
    else:
        print "REQUEST"
        oauth_token = request.cookies.get('linkedin_oauth_%s' % cfg.get('auth', 'consumer_key'))
        oauth_token = urllib.unquote(oauth_token)
        oauth_token = json.loads(oauth_token)
        access_token = oauth_token.get('access_token')

    access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken?scope=r_network'
    consumer = oauth2.Consumer(
        key=cfg.get('auth', 'consumer_key'),
        secret=cfg.get('auth', 'consumer_secret')
    )
    client = oauth2.Client(consumer)
    resp, content = client.request(access_token_url, "POST", body='xoauth_oauth2_access_token=%s' % access_token)

    qsl = urlparse.parse_qsl(content)
    request_token = dict(qsl)
    if 'oauth_problem' in request_token:
        return "BAD"
    oauth_secret = request_token.get('oauth_token_secret')
    oauth_token = request_token.get('oauth_token')
    session['linkedin_oauth_token'] = oauth_token
    session['linkedin_oauth_secret'] = oauth_secret
    print oauth_token
    print oauth_secret
    return "GOOD"


@app.route("/profile/<profileId>")
def profile(profileId):
    authCookie = request.cookies.get('linkedin_oauth_%s' % cfg.get('auth', 'consumer_key'))
    authString = urllib.unquote(authCookie)

    # profile
    LinkedIn = LinkedInApi.LinkedInApi(session['linkedin_oauth_token'], session['linkedin_oauth_secret'])
    profile = parser.parse(LinkedIn.profile(profileId))
    print
    #print profile
    print
    positions = profile['positions']['values']
    raw = nlp.ascii(parser.raw(profile))
    tokens = nlp.tokenize(raw)
    tokens = nlp.normalize(tokens)
    token_str = ' '.join(tokens)
    freq = ' '.join(nlp.freq_dist(tokens, 3))
    # connections
    parser_parse = parser.parse(LinkedIn.connections(profileId))
    # we can't (yet) get to our connections connections
    if 'message' in parser_parse.keys():
        print parser_parse
        connections = []
    else:
        connections = parser_parse['values']
    # context
    context = {}
    context['id'] = authString
    context['profile'] = profile
    context['positions'] = positions
    context['tokens'] = token_str
    context['connections'] = connections
    context['frequent'] = freq
    return render_template('profile.html', **context)


if __name__ == "__main__":
# app.run()
    app.run(debug=True)

