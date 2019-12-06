import requests
import json

class BasestationNetwork:
    def __init__(self, url):
        self.url = url

    def sendController(self, controllerDictionary):
        requests.post(self.url + "controller/update", data = {'updateDict': json.dumps(controllerDictionary)})
