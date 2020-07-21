from json import JSONDecodeError
import requests
import json
# from pprint import pprint

class Pokemon:
    def __init__(self):
        try:
            self.name = input("choose a pokemon?")
            self.address = f"https://pokeapi.co/api/v2/pokemon/{self.name}/"
            self.req_response = requests.get(self.address)
            self.all_info = self.req_response.json()
            self.abilities = []
            self.effects = []
            self.moves = []
            self.stats = []
            self.abilities_effects = self.get_abilities_effects()
            self.get_moves()
            self.base_stats()
            self.type = self.all_info['types'][0]['type']['name']
            self.weight = self.all_info['weight']
            self.height = self.all_info['height']
            self.write_to_file()
        except JSONDecodeError:
            print("This pokemon is not real")
    def get_abilities_effects(self):
        ability_url = []
        for row in self.all_info['abilities']:
            self.abilities.append(row['ability']['name'])
            ability_url.append(row['ability']['url'])
        for url in ability_url:
            get_effect = requests.get(url)
            effect_response = get_effect.json()['effect_entries']
            for row in effect_response:
                if row['language']['name'] == 'en':
                    append_with = row['short_effect']
                    self.effects.append(append_with)
        return f"{list(map(lambda x, y: (x, y), self.abilities, self.effects))}"
    def get_moves(self):
        for row in self.all_info['moves']:
            self.moves.append(row['move']['name'])
        return f"{self.moves}"
    def base_stats(self):
        for row in self.all_info['stats']:
            self.stats.append(f"{row['stat']['name']} : {row['base_stat']}")
        return f"{self.stats}"
    def write_to_file(self):
        with open(f"pokemon_{self.name}_api.txt", "a") as pokefile:
            pokefile.writelines(f"Name: {self.name}\nType:{self.type}\nHeight:{self.height}\nWeight:{self.weight}\n\n"
                                f"Abilities and Effect: {self.abilities_effects}\n\nMoves: {self.moves}\n\n"
                                f"Base stats: {self.stats} ")

poke1 = Pokemon()
print(poke1.get_abilities_effects())

print(poke1.abilities)