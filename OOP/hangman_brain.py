from random import choice
from hangman_game import Game

word_list = ["anaconda", "supernova", "psychedelic", "autodidact"]

class Brain(Game):

    def __init__(self, attempts=8):
        #Game.__init__(self)
        self.game = Game()
        self.user_name = ''
        self.attempts = attempts
        self.word = choice(word_list)
        self.word_length = len(self.word)
        self.first_letter = self.word[0]
        self.last_letter = self.word[-1]
        self.initial_status = []
        self.play_again = True

    def hangman_initiation(self):
        self.user_name = input("Hello user! What is your name? \n")
        game_choice = input(f"{self.user_name} do you want the easy version (first and last letters given)? Y/N \n")
        self.initial_status = ["_"] * self.word_length  # INITIALIZING hidden word
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
        print(self.initial_status)

    def hangman_win(self):
        word = []
        for letter in self.word:
            word.append(letter)
        print(word)
        print(f"Congratulations {self.user_name}! You won!!!")

    def hangman_lose(self):
        print(f"Sorry {self.user_name} but this is not the right word. You lost!")

    def hangman_renew(self):
        user_choice = input("Would you like to play again? Y/N\n")
        if user_choice.upper() == 'y' or user_choice.upper() == 'yes':
            print("Let's do this!!!")
            self.play_again = True
        else:
            print("It was a pleasure!!!")
            self.play_again = False
