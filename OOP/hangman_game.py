from hangman_brain import Brain

class Game(Brain):

    def __init__(self):
        #Brain.__init__(self)
        self.brain = Brain()
        self.guess = ''
        self.guesses_list = []
        self.total_guesses = 0

    def make_guess(self):
        self.guess = input("Make a guess:  \n")
        while self.guess in self.guesses_list:
            self.guess = input(f"You have already used {self.guess}. Make another guess:  \n")

    def update_guess_list(self):
        self.guesses_list.append(self.guess)
        self.total_guesses = len(self.guesses_list)
        return self.guesses_list

print("hello")
word1 = Brain()
game1 = Game()
while game1.total_guesses < 5:
    game1.make_guess()
    game1.update_guess_list()
    print(f"Your guesses so far are: {self.guesses_list}")


# while game1.total_guesses < 5:
#     guess = input("Make a guess:  \n")
#     while guess in game1.guesses_list:
#         guess = input(f"You have already used {guess}. Make another guess:  \n")
#     print(game1.update_guess_list(guess))
#     print(f"You made {game1.total_guesses} guess(es) so far!")
#
#     if game1.total_guesses == 4:
#         guess = input("Make your final guess:  \n")
#         while guess in game1.guesses_list:
#             guess = input(f"You have already used {guess}. Make another guess:  \n")
#
#         game1.total_guesses = 5
#         print("You have made the max number of guesses allowed.")

