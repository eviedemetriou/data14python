import requests
import json
from pprint import pprint

# # Having a single postcode
# address = "https://api.postcodes.io/postcodes/EN4 8RY"
# req_response = requests.get(address)  # use .get() for single postcode
#
# print(req_response)
# print(type(req_response))
# print(req_response.status_code)
# print(req_response.headers)
# print(req_response.content, "\n")
# # with .json() req_response turns into 'dict' type
# # pprint gives a nice format that is easily readible
# pprint(req_response.json())
# pprint(type(req_response.json()))
#
# print(f"Eastings: {req_response.json()['result']['eastings']}, Northings: {req_response.json()['result']['northings']}")
# print(f"The nuts code: {req_response.json()['result']['codes']['nuts']}")  # when keys inside f-string they have to take single quotes
# # Or: result = req_response.json()["result"] .... print(result["codes"]["nuts"])

# HTTP Status Codes
# 404 - Page Not Found
# 200 - Ok


# Having multiple postcodes - requests.post()

dict_body = {"postcodes": ["EN4 8RY", "B7 4BB"]}  # class 'dict'
json_body = json.dumps(dict_body)  # class 'str'
headers = {"Content-Type": "application/json"}
address = "https://api.postcodes.io/postcodes/"

req_response = requests.post(address, headers=headers, data=json_body)  # for many postcodes use .post()

print(req_response)
print(type(req_response))
print(req_response.headers)
print(req_response.content, "\n")

# Two ways to print the main keys of the dictionary
print(req_response.json().keys())
for i in req_response.json():
    print(i, req_response.json()[i])  # can see key: value pairs on different lines

print("\n")
#pprint(req_response.json()["result"])  # prints all postcode results in a nice format
for postcode in req_response.json()['result']:
    print(postcode)  # prints each postcode entry results on a single line
    result = postcode['result']
    print(f"Postcode: {result['postcode']}; Eastings: {result['eastings']}; Northings: {result['northings']}; \
NUTS code: {result['codes']['nuts']}")
