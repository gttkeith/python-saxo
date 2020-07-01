import json
import traceback
from pysaxo import Session

PARAMS_PATH = 'params.json'

params = json.loads(open(PARAMS_PATH,'r').read())
APP_KEY = params.get('app_key')
AUTH_ENDPOINT = params.get('auth_endpoint')
TOKEN_ENDPOINT = params.get('token_endpoint')
SECRET = params.get('secret')

a = Session(APP_KEY, AUTH_ENDPOINT, TOKEN_ENDPOINT, SECRET)

print("[Authorised, use a.get(uri) for API access]")
exit=False
while exit is False:
    cmd=input("> ")
    try:
        out=eval(cmd)
        print(out)
    except:
        print("\n** EXCEPTION **\n",traceback.format_exc(),"\n")