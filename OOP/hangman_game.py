
class Game():

    def __init__(self):
        self.guess = ''
        self.guesses_list = []
        self.total_guesses = 0

    def make_guess(self):
        user_option = input("Do you want to guess a letter (type '1') or the word (type '2')? ")
        if user_option == '1':
            self.guess = input("Make a guess (letter): \n")
            while self.guess in self.guesses_list:
                self.guess = input(f"You have already used {self.guess}. Make another guess:\n")
        else:
            self.guess = input("Type the word you are thinking: \n")

    def update_guess_list(self):
        self.guesses_list.append(self.guess)
        self.total_guesses = len(self.guesses_list)
        #print(f"You have made {self.total_guesses} guess.")
        print(f"Your guesses so far are: {self.guesses_list}")

