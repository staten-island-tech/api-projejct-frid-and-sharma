import requests
import json
from string import capwords

response_API = requests.get('https://dog.ceo/api/breeds/list/all')
data=response_API.text
parse_json=json.loads(data)
bre=parse_json["message"]
thing=bre.keys()
breeds=[item.capitalize() for item in thing]