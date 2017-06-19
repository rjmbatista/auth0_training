import json

from auth0.v3.authentication import GetToken
from auth0.v3.authentication import Users

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import session

import urllib

APP = Flask(__name__, static_url_path='')
APP.secret_key = 'secretkey'
APP.debug = True

AUTH0_DOMAIN = ''
AUTH0_CLIENT_ID = ''
AUTH0_CLIENT_SECRET = ''
AUTH0_CALLBACK_URL = 'http://localhost:3000/callback'
AUTH0_AUDIENCE_API = 'http://localhost:3000'
#AUTH0_AUDIENCE_API = 'https://'+AUTH0_DOMAIN+'/userinfo'
AUTH0_RETURN_TO_URL = urllib.quote('http://localhost:3000')

@APP.route('/')
def index():
    return render_template('index.html', auth0_domain=AUTH0_DOMAIN, auth0_client_id=AUTH0_CLIENT_ID, 
        auth0_audience_api=AUTH0_AUDIENCE_API, auth0_callback_url=AUTH0_CALLBACK_URL)

@APP.route('/callback')
def callback_handling():
    code = request.args.get('code')
    get_token = GetToken(AUTH0_DOMAIN)
    auth0_users = Users(AUTH0_DOMAIN)
    token = get_token.authorization_code(AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, code, AUTH0_CALLBACK_URL)
    user_info = auth0_users.userinfo(token['access_token'])
    return render_template('dashboard.html',
                           user=json.loads(user_info), token=token)

@APP.route('/logout')
def logout():
    session.clear()
    return redirect('https://' + AUTH0_DOMAIN + '/v2/logout?returnTo=' + AUTH0_RETURN_TO_URL + '&client_id=' + AUTH0_CLIENT_ID)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=3000)