from linkedin import config, api, parser, text
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    cfg = config.config_parser()
    consumer_key = cfg.get('auth', 'consumer_key')
    return render_template('index.html', key=consumer_key)


@app.route("/profile")
def profile():
    id = request.args.get('linkedin-id', '')

    # profile
    json_profile = api.profile()
    profile = parser.parse(json_profile)
    positions = profile['positions']['values']
    positions_str = parser.positions_str(positions)
    tokens = text.tokenize(positions_str)
    token_str = ' '.join(text.meaning_words(tokens))
    freq = ' '.join(text.freq_dist(tokens, 3))

    # connections
    json_conn = api.connections()
    connections = parser.parse(json_conn)['values']

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

