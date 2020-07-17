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

word1 = Brain()

while word1.game.play_again == True:  # Keep playing as long as user wants to continue
    word1.reset()  # Resetting and starting over
    word1.hangman_initiation()  # Initializing word to be presented to user
    while word1.game.total_guesses < word1.attempts:
        word1.game.make_guess()  # Make a guess

        if len(word1.game.guess) > 1:  # Case when user chooses to guess the whole word - Check for win/loss
            if word1.game.guess.lower() == word1.word:
                word1.hangman_win()
            else:
                word1.hangman_lose()
            break

        word1.hangman_update()  # UPDATE letters in word
        if '_' not in word1.initial_status:  # Check for win
            print(f"*** CONGRATULATIONS {word1.game.user_name.upper()}! YOU WON!!!*** \n")
            break
        word1.game.update_guess_list()

        if word1.game.total_guesses == word1.attempts - 1:  # Distinct process for the FINAL GUESS of the user
            print("You only have ONE MORE guess.")
            word1.game.make_guess()  # Make a guess

            if len(word1.game.guess) > 1:  # Case when user chooses to guess the whole word - Check for win/loss
                if word1.game.guess == word1.word:
                    word1.hangman_win()
                else:
                    word1.hangman_lose()
                break

            word1.hangman_update()  # UPDATE word with letters
            if '_' not in word1.initial_status:  # Check for win or loss
                print(f"*** CONGRATULATIONS {word1.game.user_name.upper()}! YOU WON!!! ***\n")
            else:
                print(f"*** Good try {word1.game.user_name} BUT YOU LOST! ***\n")
            break

    word1.hangman_renew()  # Choice to play again