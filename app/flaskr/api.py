import requests
import json


response_API = requests.get('https://dog.ceo/api/breeds/list/all')
data=response_API.text
parse_json=json.loads(data)
breeds=parse_json["message"]
print(breeds.keys())