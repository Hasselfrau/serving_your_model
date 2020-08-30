import requests
from conf import *

def json_request(data):
    json_obj = data.to_json(orient='table')
    r = requests.post(URL_BASE_JSON, json=json_obj)
    return f'input:\n{json_obj[:2000]}\noutput: {r.text}'
