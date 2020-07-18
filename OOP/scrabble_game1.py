# Computer generating words based on a list of words given - not interactive
from random import choice

letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E',
               'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J','K',
               'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
               'R', 'R', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
Scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }

word_list = ['to', 'in', 'on', 'at', 'and', 'for', 'far', 'sun', 'him', 'her', 'the', 'red', 'kid', 'kite', 'media', 'rope',
             'boat', 'road', 'fruit', 'cloth', 'slide',  'above', 'plate', 'fresh', 'horse', 'cream', 'scream', 'certain']

class Scrabble:

    def __init__(self):
        self.tiles = []
        self.word_score = 0
        self.word_score_list = []
        self.total_score = 0
        self.word_chosen = ''
        self.play_again = True

    def tile_generation(self):
        if self.word_chosen == '':
            for i in range(7):
                self.tiles.append(choice(letter_list))
            return self.tiles
        else:
            for i in self.word_chosen:
                index = self.tiles.index(i.upper())
                self.tiles.pop(index)
                self.tiles.append(choice(letter_list))
            return self.tiles

    def word_check(self):
        words_found = []
        for word in word_list:
            letters = [word.upper()[i:i+1] for i in range(len(word))]
            if set(letters).issubset(set(self.tiles)):
                # subset check might not be valid if word contains letter more than once but in tiles it is only present once
                words_found.append(word)
        if len(words_found) == 0:
            print("No words found -> Generate 7 new tiles\n")
            self.word_chosen = ''
            self.tiles.clear()
            return self.word_chosen
        elif len(words_found) == 1:
            self.word_chosen = words_found[0]
            print(f"The only word found is '{self.word_chosen}'.")
            return self.word_chosen
        elif len(words_found) > 1:
            for i in range(len(words_found)-1):
                if self.get_word_score(words_found[i]) > self.get_word_score(words_found[i+1]):
                    words_found[i], words_found[i+1] = words_found[i+1], words_found[i]
            self.word_chosen = words_found[-1]
            print(f"The word found with the highest score is '{self.word_chosen}'.")
            return self.word_chosen

    def get_word_score(self, word=None):
        if word == None:  # used when only a single word has been found, assigned as word_chosen
            self.word_score = 0
            for i in self.word_chosen:
                self.word_score += Scores[i.upper()]
            self.word_score_list.append(self.word_score)
            return f"This word is worth {self.word_score} points.\n"
        else:  # used when more than one words have been found in word_check(), to find the one with the highest score
            self.word_score = 0
            for i in word:
                self.word_score += Scores[i.upper()]
            self.word_score_list.append(self.word_score)
            return f"This word is worth {self.word_score} points.\n"

    def want_to_play(self):
        choice = input("Do you want to have another round? Y/N\n")
        if choice.upper() == 'Y' or choice.upper() == 'YES':
            pass
        else:
            self.play_again = False
            print(f"Your total score is {sum(self.word_score_list)}\n")  # Calculated wrong.. haven't checked why
            print("GOODBYE!!!")
            return self.play_again


game = Scrabble()

while game.play_again == True:
    print(game.tile_generation())
    game.word_check()
    while game.word_chosen == '':
        print(game.tile_generation())
        game.word_check()
    print(game.get_word_score())
    game.want_to_play()
