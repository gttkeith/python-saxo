import json
import pprint
import traceback
from pysaxo import Session

PARAMS_PATH = 'params.json'

params = json.loads(open(PARAMS_PATH,'r').read())
APP_KEY = params.get('app_key')
AUTH_ENDPOINT = params.get('auth_endpoint')
TOKEN_ENDPOINT = params.get('token_endpoint')
SECRET = params.get('secret')

access = Session(APP_KEY, AUTH_ENDPOINT, TOKEN_ENDPOINT, SECRET)

print("[Authorised, use access.get/post/put/delete(uri) for API access]")
exit=False
pp = pprint.PrettyPrinter(indent=2)
while exit is False:
    cmd=input("> ")
    try:
        out=eval(cmd)
        pp.pprint(out)
    except:
        print("\n** EXCEPTION **\n",traceback.format_exc(),"\n")