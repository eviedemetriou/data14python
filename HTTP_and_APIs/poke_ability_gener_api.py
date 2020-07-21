import requests
import json
from pprint import pprint

generation = {"limber": 3, "imposter": 5}

class PokeAbilityGeneration:

    def __init__(self, ability):
        self.generation_address = f"https://pokeapi.co/api/v2/generation/{generation[ability]}"
        self.generation_request = requests.get(self.generation_address)
        self.generation_response_json = self.generation_request.json()
        #self.generation = generation

    def show_ability_generation_details(self):
        print("\tGeneration details:")
        for key in self.generation_response_json:
            print(f"\t\tKEY {key}, VALUE {self.generation_response_json[key]}")
        #pprint(self.generation_response_json)
