import requests
import json
from pprint import pprint

dict_body = {"postcodes": ["EN4 8RY", "B7 4BB"]}
json_body = json.dumps(dict_body)
headers = {"Content-Type": "application/json"}
address = "https://api.postcodes.io/postcodes/"

req_response = requests.post(address, headers=headers, data=json_body)

pprint(req_response.json())
print(type(req_response.json()))
# for i in req_response:
#     pprint(i)

#result = req_response.json()["result"]
#print(result)

#for row in result:
#    print(row)

for postcode in req_response.json()['result']:
    #print(postcode)
    result = postcode['result']
    print(f"Postcode: {result['postcode']}; Eastings: {result['eastings']}; Northings: {result['northings']}; NUTS code: {result['codes']['nuts']}")


# my_house = Postcode("")
# print(my_house.)


# address = "https://api.postcodes.io/postcodes/EN4 8RY"
# req_response = requests.get(address)

#print(req_response)
#print(type(req_response))
#print(req_response.status_code)
#print(req_response.headers)
#print(req_response.content)
#pprint(req_response.json())
#pprint(type(req_response.json()))

# HTTP status codes
#484 - Pge not found
#288 - Ok

#result = req_response.json()["result"]
#print(result["nuts"])
#print((req_response.json()["result"]["eastings"]), req_response.json()["result"]["northings"])
#print(f"The nuts code: {req_response.json()["result"]["nuts"]}")

