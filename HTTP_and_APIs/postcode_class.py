import requests
import json
from pprint import pprint

class SinglePC:

    def __init__(self, postcode):
        self.postcode = postcode
        self.address = f"https://api.postcodes.io/postcodes/{self.postcode}"
        self.request = requests.get(self.address)
        self.response_json = self.request.json()

    def show_details(self):
        print("\n", self.postcode)
        for key in self.response_json:
            print(f"\tKEY {key}, VALUE {self.response_json[key]}")
        # pprint(self.response_json)  # nice format


# # Creating multiple postcode objects using a list of postcodes
# postcodes = ["EN4 8RY", "EN5 3TU"]
# pc_objects = []
#
# for elem in postcodes:
#     # SinglePC(elem).show_details()  # Creating responses for objects that we don't want to store
#     pc_objects.append(SinglePC(elem))
#     SinglePC(elem).show_details()
# print(pc_objects)



class MultiplePC:

    def __init__(self, postcodes: dict):
        self.postcodes = postcodes
        self.json_body = json.dumps(self.postcodes)
        self.headers = {"Content-Type": "application/json"}
        self.address = f"https://api.postcodes.io/postcodes/"
        self.request = requests.post(self.address, headers=self.headers, data=self.json_body)
        self.response_json = self.request.json()


town1_pcs = {"postcodes": ["EN4 8RY", "B7 4BB"]}
town1 = MultiplePC(town1_pcs)

pprint(town1.response_json)