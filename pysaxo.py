import random
import requests
import threading

REDIR_URI = "http://gttkeith.github.io/python-saxo/authcode"

class Session:
    @staticmethod
    def new_state(stringLength=16):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        return ''.join(random.choice(chars) for i in range(stringLength))

    def parse_json(self, tokenJson):
        self.token = tokenJson.get('access_token')
        self.expires_in = int(tokenJson.get('expires_in'))
        self.refresh = tokenJson.get('refresh_token')
    
    def periodic_token_refresh(self):
        self.expires_in -= 1
        if self.expires_in < 60:
            tokenJson = requests.post(self.token_endpoint, params={'grant_type':'refresh_token','refresh_token':self.refresh,'redirect_uri':REDIR_URI,'client_id':self.app_key,'client_secret':self.secret}).json()
            self.parse_json(tokenJson)

    def __init__(self,app_key,auth_endpoint,token_endpoint,secret):
        self.app_key = app_key
        self.auth_endpoint = auth_endpoint
        self.token_endpoint = token_endpoint
        self.secret = secret
        r = requests.get(self.auth_endpoint, params={'response_type':'code','client_id':self.app_key,'state':Session.new_state(),'redirect_uri':REDIR_URI})
        print("Log in and obtain authcode: " + r.url)
        authcode = input("Paste authcode: ")
        tokenJson = requests.post(self.token_endpoint, params={'grant_type':'authorization_code','code':authcode,'redirect_uri':REDIR_URI,'client_id':self.app_key,'client_secret':self.secret}).json()
        self.parse_json(tokenJson)
        threading.Timer(1, self.periodic_token_refresh).start()