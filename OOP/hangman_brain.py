from random import choice

word_list = ["anaconda", "supernova", "psychedelic", "autodidact"]

class Brain:

    def __init__(self):
        self.word = choice(word_list)
        self.word_length = len(self.word)
        self.first_letter = self.word[0]
        self.last_letter = self.word[-1]

    def hangman_update(self, guess : str, initial):
        index = []
        for i in range(0, self.word_length):
            if self.word[i] == guess:
                index.append(i)
        for j in index:
            initial[j] = guess
        print(initial)

    def hangman_initiation(self):
        initial = ["_"] * self.word_length
        game_choice = input("Do you want the easy version (first and last letters given)? Y/N \n")
        if game_choice.upper() == 'Y' or game_choice.upper() == 'YES':
            print("As you like!")
            initial[0] = self.first_letter
            initial[-1] = self.last_letter
            print(initial)
            for i in range(10):
                guess = input("Make a guess:  \n")
                self.hangman_update(guess, initial)
        else:
            print(initial)
            for i in range(10):
                guess = input("Make a guess:  \n")
                self.hangman_update(guess, initial)


word1 = Brain()
word1.hangman_initiation()

