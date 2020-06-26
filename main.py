import json
from pysaxo import Session

PARAMS_PATH = 'params.json'

params = json.loads(open(PARAMS_PATH,'r').read())
APP_KEY = params.get('app_key')
AUTH_ENDPOINT = params.get('auth_endpoint')
TOKEN_ENDPOINT = params.get('token_endpoint')
SECRET = params.get('secret')

access = Session(APP_KEY, AUTH_ENDPOINT, TOKEN_ENDPOINT, SECRET)