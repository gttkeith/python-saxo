import json
import random
import requests
import threading

PARAMS_PATH = 'params.json'

params = json.loads(open(PARAMS_PATH, 'r').read())
APPKEY = params.get('app_key')
AUTH_ENDPOINT = params.get('auth_endpoint')
TOKEN_ENDPOINT = params.get('token_endpoint')
REDIR_URL = params.get('redir_uri')
SECRET = params.get('secret')

class Session:
    @staticmethod
    def new_state(stringLength=16):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        return ''.join(random.choice(chars) for i in range(stringLength))

    def parse_json(self, tokenJson):
        self.token = tokenJson.get('access_token')
        self.expires_in = tokenJson.get('expires_in')
        self.refresh = tokenJson.get('refresh_token')
    
    def periodic_token_refresh(self):
        threading.Timer(1, periodic_token_refresh).start ()
        self.refresh -= 1
        if self.refresh < 60:
            tokenJson = requests.post(TOKEN_ENDPOINT, params={'grant_type':'refresh_token','refresh_token':self.refresh,'redirect_uri':REDIR_URL, 'client_id':APPKEY, 'client_secret':SECRET}).json()
            self.parse_json(tokenJson)
            return True

    def __init__(self):
        r = requests.get(AUTH_ENDPOINT, params={'response_type':'code', 'client_id':APPKEY, 'state':Session.new_state(), 'redirect_uri':REDIR_URL})
        print("Login and obtain authcode: " + r.url)
        authcode = input("Paste authcode: ")
        tokenJson = requests.post(TOKEN_ENDPOINT, params={'grant_type':'authorization_code','code':authcode,'redirect_uri':REDIR_URL, 'client_id':APPKEY, 'client_secret':SECRET}).json()
        self.parse_json(tokenJson)
        self.periodic_token_refresh()

access = Session()