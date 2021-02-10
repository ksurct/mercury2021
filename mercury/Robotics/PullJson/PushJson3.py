import requests
import json

url = "http://10.132.159.140:8000/sendjson/"
myobj = {'somekey': 'somevalue'}


x = requests.put(url, json=myobj)

response = requests.get(url)
todos = json.loads(response.text)
print(todos)

print(x.text)


