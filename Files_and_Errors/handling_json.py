import json
from pprint import pprint

## Reading json file
with open("film.json", "r") as jsonfile:
    film = json.load(jsonfile)  # also have .loads() which will convert into string

print(film)  # prints key:value pairs in a line
print(type(film))  # dictionary!
print(film["The Fugitive"]["Author"])  # using the dictionary to get keys/values
pprint(film)  # prints dictionary nicely with keys in alphabetic line


## Writing into json file
# film = {
#     "name": "The Godfather",
#     "length": 178,
#     "cast": {"Al Pachino": "Michael"}
# }
# print(film)  # film is a dictionary
# print(json.dumps(film))  # .dumps() converts dictionary to a string
#
# with open("Godfather.json", "w") as jsonfile:
#     json.dump(film, jsonfile)  # takes dic (film) and dumps it in given file (jsonfile)


## Creting class whose objects will be given attributes from a json (dict) file
class Film:

    def __init__(self, name, length, cast):
        self.name = name
        self.length = length
        self.cast = cast

with open("Godfather.json", "r") as jsonfile:
    film_dict = json.load(jsonfile)

# Create instance of class and pass in attributes from the film_dict object
godfather = Film(film_dict["name"], film_dict["length"], film_dict["cast"])
print(godfather.name, godfather.length, godfather.cast)

## OR
    def __init__(self, json_file_name):
        with open(jsonfilename) as jsonfile:
            film_dict = json.load(jsonfile)
        self.name = film_dict["name"]
        self.length = film_dict["length"]
        self.cast = cast["cast"]

godfather = Film("Godfather.json")
print(godfather.name, godfather.length, godfather.cast)
