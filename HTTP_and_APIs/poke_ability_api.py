#from poke_ability_gener_api import PokeAbilityGeneration
import requests
import json
from pprint import pprint

class PokeAbilities:

    def __init__(self, single_ability):
        self.single_ability = single_ability
        self.ability_address = f"https://pokeapi.co/api/v2/ability/{self.single_ability}"
        self.ability_request = requests.get(self.ability_address)
        self.ability_response_json = self.ability_request.json()
        self.ability_generation_url = self.ability_response_json["generation"]["url"]
        self.generation = self.ability_response_json["generation"]["name"]

    def show_ability_details(self):
        print("\n" + self.single_ability + " details:")
        for key in self.ability_response_json:
            print(f"\tKEY {key}, VALUE {self.ability_response_json[key]}")
        #pprint(self.ability_response_json)  # nice format

    def show_ability_generation(self):
        print("Ability generation:")
        print(self.generation)


if __name__ == "__main__":
    poke = PokeAbilities("limber")
    poke.show_ability_details()
    poke.show_ability_generation()
    print(poke.ability_generation_url)


# class PokeAbilityGeneration(PokeAbilities):
#
#     def __init__(self, single_ability):
#         super().__init__(single_ability)
#         self.generation_url = super().ability_generation_url
#         self.generation_address = f"https://pokeapi.co/api/v2/generation/{self.generation_url}"
#         self.generation_request = requests.get(self.generation_address)
#         self.generation_response_json = self.generation_request.json()
#         #self.generation = generation
#
#     def show_ability_generation_details(self):
#         print("\n" + self.generation + " details:")
#         for key in self.generation_response_json:
#             print(f"\tKEY {key}, VALUE {self.generation_response_json[key]}")
#         # pprint(self.ability_response_json)  # nice format
#
# gen = PokeAbilityGeneration("limber")
# pprint(self.generation_response_json)