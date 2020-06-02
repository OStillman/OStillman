import json
import requests

class HandleRequest():
    def __init__(self, response=None):
        self.simpleResponse()

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, response):
        self._response = response

    def simpleResponse(self):
        response = requests.get('http://localhost:83/ghome')
        self.response = response.text
