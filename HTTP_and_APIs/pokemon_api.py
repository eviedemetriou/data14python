import requests
import json
from pprint import pprint
from poke_ability_api import PokeAbilities
from poke_ability_gener_api import PokeAbilityGeneration

class SinglePokemon():

    def __init__(self, poke_name):
        #super().__init__(single_ability)
        self.poke_name = poke_name
        self.address = f"https://pokeapi.co/api/v2/pokemon/{self.poke_name}"
        self.request = requests.get(self.address)
        self.response_json = self.request.json()
        self.abilities = self.response_json['abilities']
        self.base_experience = self.response_json['base_experience']
        self.forms = self.response_json['forms']

    def show_all_details(self):
        print("\n" + self.poke_name)
        for key in self.response_json:
            print(f"\tKEY {key}, VALUE {self.response_json[key]}")
        print("\n")
        #pprint(self.response_json)  # nice format

    def show_abilities(self):
        print(f"Abilities of {self.poke_name}:")
        for i in self.abilities:
            print(i["ability"]["name"])

    def show_ability_details(self):
        for i in self.abilities:
            poke_ability = PokeAbilities(i["ability"]["name"])
            poke_ability.show_ability_details()

    def show_ability_generation(self):
        print(f"Generation of abilities of {self.poke_name}")
        for i in self.abilities:
            poke_ability = PokeAbilities(i["ability"]["name"])



poke = SinglePokemon("ditto")
#poke.show_abilities()
poke.show_ability_details()
#poke.show_all_details()

# poke_ditto = SinglePokemon("ditto")
# poke_ditto.show_all_details()
# poke_ditto.show_abilities()
#
# ditto_abilities = {"limber": 7, "imposter": 150}
# for ability in ditto_abilities:
#     ditto = PokeAbilities(ability)
#     ditto.show_ability_details()
#     ditto = PokeAbilityGeneration(ability)
#     ditto.show_ability_generation_details()


## Class inheritance
# ditto = SinglePokemon("ditto", "limber")
# ditto.show_all_details()
#
# ditto_abilities = {"limber": 7, "imposter": 150}
# for ability in ditto_abilities:
#     ditto = SinglePokemon("ditto", ability)
#     ditto.show_ability_details()