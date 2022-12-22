import requests
import json


response_API = requests.get('https://dog.ceo/api/breeds/image/random')
data=response_API.text
parse_json=json.loads(data)
img=parse_json["message"]