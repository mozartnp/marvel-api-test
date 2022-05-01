from decouple import config
import hashlib
import requests

def cabecalho():
    apikey = config('PUBLIC_KEY')
    pr_key = config('PRIVATE_KEY')
    ts = "1"
    hash_str = ts + pr_key + apikey
    hash = hashlib.md5((hash_str).encode("utf-8"))
    hash = hash.hexdigest()
    cabecalho_string = ("?ts={}&apikey={}&hash={}").format(ts, apikey, hash)
    return cabecalho_string

def get_marvel_json(url_sufix, cabecalho_string):
    url_prefix = "http://gateway.marvel.com/v1/public/"
    url = url_prefix + url_sufix + cabecalho_string
    try:
        response = requests.get(url)
        response_json = response.json()
        if response.status_code != 200:
            response_json = False
    except ValueError:
        response, response_json = False, False
    return response_json