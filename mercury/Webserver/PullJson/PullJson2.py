import requests
post_data = { 'name': 'Gladys'}
response = requests.post("http://10.132.159.140:8000/sendjson/", data=post_data)

