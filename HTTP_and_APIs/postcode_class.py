import requests
import json
from pprint import pprint

#dict_body = {"postcodes": ["EN4 8RY", "B7 4BB"]}

class Postcode:

    def __init__(self, postcode):
        self.postcode = postcode
        #self.json_body = json.dumps(dict_body)
        #self.headers = {"Content-Type": "application/json"}
        self.address = f"https://api.postcodes.io/postcodes/{self.postcode}"
        self.req_response = requests.get(self.address)

    def show_details(self):
        pprint(self.req_response.json())

home = Postcode("EN4 8RY")

home.show_details()

postcodes = []
pc_objects = []

for postcode in postcodes:
    pc_objects.append(Post(postcode))


