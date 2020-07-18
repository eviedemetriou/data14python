from random import choice

letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E',
               'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J','K',
               'L', 'L', 'L', 'M', 'M', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
               'R', 'R', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'V', 'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
Scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }

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

    def word_found_check(self):
        self.word_chosen = ''
        while self.word_chosen == '':
            x = input("Can you spot any word? Y/N ")
            if x.upper() == "Y" or x.upper() == "YES":
                word = input("Type it here: ")
                if set([word.upper()[i] for i in range(len(word))]).issubset(set(self.tiles)):
                    # subset check might not be valid if word contains letter more than once but in tiles it is only present once
                    print("Well done! The word you have chosen is a valid word!")
                    self.word_chosen = word
                    return self.word_chosen
                else:
                    print(f"Sorry but this word is not possible! Have another go... \n")
                    self.word_chosen = ''  # stays an empty string and keeps looping
            else:
                print("No words found -> Generate 7 new tiles\n")
                self.word_chosen = ''  # stays an empty string but break out of loop
                self.tiles = []
                break

    def get_word_score(self):
        self.word_score = 0
        for i in self.word_chosen:
            self.word_score += Scores[i.upper()]
        self.word_score_list.append(self.word_score)
        return f"This word is worth {self.word_score} points.\n"

    def want_to_play(self):
        choice = input("Do you want to have another round? Y/N\n")
        if choice.upper() == 'N' or choice.upper() == 'NO':
            self.play_again = False
            print(f"Your total score is {sum(self.word_score_list)}\n")
            print("GOODBYE!!!")
            return self.play_again


game1 = Scrabble()

while game1.play_again == True:
    print(game1.tile_generation())
    game1.word_found_check()
    while game1.word_chosen == '':
        print(game1.tile_generation())
        game1.word_found_check()
    print(game1.get_word_score())
    game1.want_to_play()
