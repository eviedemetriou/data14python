from random import choice
from hangman_game import Game

word_list = ["anaconda", "supernova", "psychedelic", "autodidact", "inconsequential"]

class Brain(Game):

    def __init__(self, attempts=8):
        #Game.__init__(self)
        self.game = Game()
        self.attempts = attempts
        self.word = choice(word_list)
        self.word_length = len(self.word)
        self.first_letter = self.word[0]
        self.last_letter = self.word[-1]
        self.initial_status = []
        #self.reset()
        #self.play_again = True

    #def reset(self):

    def hangman_initiation(self):  # INITIALIZING hidden word - choose easy/hard version of game
        self.game.user_name = input("Hello user! What is your name? \n")
        game_choice = input(f"{self.game.user_name} do you want the easy hangman version (first and last letters given)? Y/N \n")
        self.initial_status = ["_"] * self.word_length
        if game_choice.upper() == 'Y' or game_choice.upper() == 'YES':
            print("As you like!\n")
            self.initial_status[0] = self.first_letter
            self.initial_status[-1] = self.last_letter
            print(self.initial_status)
        else:
            print("As you like!\n")
            print(self.initial_status)
        print(f"You can have {self.attempts} guesses. If you don't find the word you lose! \n")

    def hangman_update(self):
        index = []
        for i in range(0, self.word_length):
            if self.word[i] == self.game.guess:
                index.append(i)
        for j in index:
            self.initial_status[j] = self.game.guess
        print(self.initial_status, "\n")

    def hangman_win(self):
        word = []
        for letter in self.word:
            word.append(letter)
        print(word)
        print(f"\n*** CONGRATULATIONS {self.game.user_name.upper()}! YOU WON!!! ***\n")

    def hangman_lose(self):
        print(f"\n*** Good try {self.game.user_name} but this is not the right word. YOU LOST! ***\n")

    def hangman_renew(self):
        user_choice = input("Would you like to play again? Y/N\n")
        if user_choice.upper() == 'Y' or user_choice.upper() == 'YES':
            self.game.play_again = True
        else:
            print("IT WAS A PLEASURE!!!")
            self.game.play_again = False

    def reset(self, attempts=8):
        self.game = Game()
        self.attempts = attempts
        self.word = choice(word_list)
        self.word_length = len(self.word)
        self.first_letter = self.word[0]
        self.last_letter = self.word[-1]
        self.initial_status = []
