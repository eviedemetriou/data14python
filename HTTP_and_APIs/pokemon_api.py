import requests
import json
from pprint import pprint
from poke_ability_api import PokeAbilities
#from poke_ability_gener_api import PokeAbilityGeneration

class SinglePokemon():

    def __init__(self, poke_name):
        try:
            #super().__init__(single_ability)
            self.poke_name = input("Choose a pokemon:")
            self.address = f"https://pokeapi.co/api/v2/pokemon/{self.poke_name}"
            self.request = requests.get(self.address)
            self.response_json = self.request.json()
            self.abilities = self.response_json['abilities']
            self.base_experience = self.response_json['base_experience']
            self.forms = self.response_json['forms']
        except JSONDecodeError:
            print("This pokemon does not exist.")

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
poke.show_abilities()
poke.show_ability_details()

