from hangman_brain import Brain

word1 = Brain()

while word1.play_again == True:

    word1.hangman_initiation()
    while word1.game.total_guesses < word1.attempts:
        word1.game.make_guess()

        if len(word1.game.guess) > 1:  # Case when user chooses to guess the whole word
            if word1.game.guess == word1.word:
                word1.hangman_win()
            else:
                word1.hangman_lose()
            break

        word1.hangman_update()  # UPDATE letters in word when applicable
        if '_' not in word1.initial_status:  # Check for WIN
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

    word1.hangman_renew()