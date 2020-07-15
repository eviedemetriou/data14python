from hangman_brain import Brain

word1 = Brain()

while word1.game.play_again == True:
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


