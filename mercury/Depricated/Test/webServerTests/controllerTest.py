import requests, json

server = 'http://localhost:8000/'

controllerDict = {
    'a': 0, 'b': 1, 'x': 2, 'y': 3, 
    'u': 4, 'd': 5, 'l': 6, 'r': 7,
    'lt': 8, 'rt': 9, 'lb': 10, 'rb': 11, 
    'lsx': 12, 'lsy': 13, 'rsx': 14, 'rsy': 15,
    'st': 16, 'se': 17
}

retVal = requests.post(server + 'controller/update', data = {'updateDict': json.dumps(controllerDict)})
#retVal = requests.get(server + 'controller/get')

print(retVal)
print(retVal.text)
#print(json.loads(retVal.text)) #used on get test

controllerDictMissingSe = {
    'a': 0, 'b': 1, 'x': 2, 'y': 3, 
    'u': 4, 'd': 5, 'l': 6, 'r': 7,
    'lt': 8, 'rt': 9, 'lb': 10, 'rb': 11, 
    'lsx': 12, 'lsy': 13, 'rsx': 14, 'rsy': 15,
    'st': 16
}

retVal = requests.post(server + 'controller/update', data = {'updateDict': json.dumps(controllerDictMissingSe)})
print(retVal)
print(retVal.text)