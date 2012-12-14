from linkedin import config, api, parser
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
    json_profile = api.profile()
    profile = parser.parse(json_profile)
    context = {}
    context['id'] = id
    context['profile'] = profile
    return render_template('profile.html', **context)

if __name__ == "__main__":
# app.run()
    app.run(debug=True)

