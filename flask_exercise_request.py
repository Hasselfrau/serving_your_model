import requests
from conf import *


def single_request(sample):
    api_dict = dict(zip(sample.columns.tolist(), sample.values.tolist()[0]))
    url_suffix = []
    for key in api_dict.keys():
        url_suffix.append(f'{key}={api_dict[key]}')
    url_suffix = '&'.join(url_suffix)
    url = URL_BASE_SINGLE + url_suffix
    res = requests.get(url)
    return f'Prediction: {res.text}'
