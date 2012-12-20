from linkedin import config, api, parser, nlp
from flask import Flask, render_template, request
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

jsD3 = Bundle('js/d3.v2.js', 'js/d3.layout.cloud.js', output='gen/packed.js')
assets.register('js_d3', jsD3)


@app.route("/")
def index():
    cfg = config.config_parser()
    consumer_key = cfg.get('auth', 'consumer_key')
    return render_template('index.html', key=consumer_key)


@app.route("/profile")
def profile():
    id = request.args.get('linkedin-id', '')
    # profile
    profile = parser.parse(api.profile())
    positions = profile['positions']['values']
    raw = nlp.ascii(parser.raw(profile))
    tokens = nlp.tokenize(raw)
    tokens = nlp.normalize(tokens)
    token_str = ' '.join(tokens)
    freq = ' '.join(nlp.freq_dist(tokens, 3))
    # connections
    connections = parser.parse(api.connections())['values']
    # context
    context = {}
    context['id'] = id
    context['profile'] = profile
    context['positions'] = positions
    context['tokens'] = token_str
    context['connections'] = connections
    context['frequent'] = freq
    return render_template('profile.html', **context)


if __name__ == "__main__":
# app.run()
    app.run(debug=True)

