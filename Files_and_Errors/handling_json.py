import json
from pprint import pprint

with open("film.json", "r") as jsonfile:
    film = json.load(jsonfile)

print(film)
print(type(film))
print(film["The Fugitive"]["Author"])
#pprint(film)

# film = {
#     "name": "The Godfather",
#     "length": 178,
#     "cast": {"Al Pachino": "Michael"}
# }
# print(film)
# print(json.dumps(film))

# with open("Godfather.json", "w") as jsonfile:
#     json.dump(film, jsonfile)

class Film:

    def __init__(self, name, length, cast):  # json_file_name
        # with open(jsonfilename) as jsonfile:
        #     film_dict = json.load(jsonfile)
        self.name = name
        self.length = length
        self.cast = cast

with open("Godfather.json", "r") as jsonfile:
    film_dict = json.load(jsonfile)

inst1 = Film(film_dict["name"], film_dict[length], film_dict[cast])

# print(inst1.name, inst1.length, inst1.cast)


