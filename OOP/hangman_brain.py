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


word1 = Brain()

word1.hangman_initiation()
while word1.game.total_guesses < word1.attempts:
    word1.game.make_guess()

    if len(word1.game.guess) > 1:  # For case when user chooses to guess the whole word
        if word1.game.guess == word1.word:
            word1.hangman_win()
        else:
            word1.hangman_lose()
        break

    word1.hangman_update()
    if '_' not in word1.initial_status:
        print(f"Congratulations {word1.user_name}! You won!!!")
        break
    word1.game.update_guess_list()

    if word1.game.total_guesses == word1.attempts - 1:  # Distinct statement for the final guess of the user
        print("You only have ONE MORE guess.")
        word1.game.make_guess()

        if len(word1.game.guess) > 1:  # For case when user chooses to guess the whole word
            if word1.game.guess == word1.word:
                word1.hangman_win()
            else:
                word1.hangman_lose()
            break

        word1.hangman_update()
        if '_' not in word1.initial_status:
            print(f"Congratulations {word1.user_name}! You have won!!!")
        else:
            print(f"Sorry {word1.user_name}, you lost!")
        break
