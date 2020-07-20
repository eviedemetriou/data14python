import requests
import json
from pprint import pprint

#abilities = {"abilities": [7, 150]}
abilities = {"limber": 7, "imposter": 150}

class PokeAbilities:

    def __init__(self, single_ability):
        #self.abilities = abilities
        self.single_ability = single_ability
        self.ability_address = f"https://pokeapi.co/api/v2/ability/{abilities[self.single_ability]}"
        self.ability_request = requests.get(self.ability_address)
        self.ability_response_json = self.ability_request.json()
        # self.poke_abilities = abilities
        # self.json_body = json.dumps(self.poke_abilities)
        # self.headers = {"Content-Type": "application/json"}
        # self.address = "https://pokeapi.co/api/v2/ability/"
        # self.request = requests.post(self.address, headers=self.headers, data=self.json_body)
        # self.response_json = self.request.json()

    def show_ability_details(self):
        print("\n" + self.single_ability + " details:")
        for key in self.ability_response_json:
            print(f"\tKEY {key}, VALUE {self.ability_response_json[key]}")
        #pprint(self.ability_response_json)  # nice format


# abilities = {"abilities": [7, 150]}
# ditto = PokeAbility(abilities)
# print(ditto.response_json)


generation = {"limber": 3, "imposter": 5}

class PokeAbilityGeneration:

    def __init__(self, ability):
        self.generation_address = f"https://pokeapi.co/api/v2/generation/{generation[ability]}"
        self.generation_request = requests.get(self.generation_address)
        self.generation_response_json = self.generation_request.json()
        #self.generation = generation

    def show_ability_generation_details(self):
        pprint(self.generation_response_json)

# limber_gen = PokeAbilityGeneration("limber")
# pprint(limber_gen)