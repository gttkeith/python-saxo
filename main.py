import csv
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

def csv_export(jsondict):
    w = csv.writer(open('out.csv','w'), dialect='excel')
    data = jsondict.get('Data')
    if data:
        schema = data[0].keys()
        w.writerow(schema)
        for row in data:
            w.writerow([row.get(k) for k in schema])
    else:
        for k,v in jsondict.items():
            w.writerow([k,v])

access = Session(APP_KEY, AUTH_ENDPOINT, TOKEN_ENDPOINT, SECRET)
print("[Authorised, use get/post/put/delete(uri) for API access]")

pp = pprint.PrettyPrinter(indent=2)
exit=False
while exit is False:
    cmd=input('> ')
    try:
        if cmd is 'exit':
            exit = True
        else:
            out=eval('access.'+cmd)
            pp.pprint(out)
            csv_export(out)
    except:
        print("\n** EXCEPTION **\n",traceback.format_exc(),"\n")