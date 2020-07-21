import requests
import json
from pprint import pprint
from poke_ability_api import PokeAbilities


class PokeAbilityGeneration:

    def __init__(self, ability):
        self.ability_obj = PokeAbilities(ability)
        self.generation = self.ability_obj.ability_response_json["generation"]["name"]
        self.generation_url = self.ability_obj.ability_response_json["generation"]["url"]
        self.generation_address = f"https://pokeapi.co/api/v2/generation/{self.generation_url}"
        self.generation_request = requests.get(self.generation_address)
        self.generation_response_json = self.generation_request.json()


    def show_ability_generation_details(self):
        print("\n" + self.generation + " details:")
        for key in self.generation_response_json:
            print(f"\tKEY {key}, VALUE {self.generation_response_json[key]}")
        # pprint(self.ability_response_json)  # nice format


poke = PokeAbilityGeneration("limber")
poke.show_ability_generation_details()