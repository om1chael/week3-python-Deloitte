from Scrabble_Checker import ScrabbleChecker

Menu = True
Game = True
while Menu:
    scrabble = ScrabbleChecker()
    scrabble.current_board()

    print("Hello lets play Scrabble")

    while Game:
        print("Here are your words:- ", "-".join(scrabble.letters))

        user_word = input("\n Give me a word:-- ")

        while not scrabble.input_check(user_word) and user_word != "quit":
            print("Your current score ", scrabble.user_score)
            print("Here are your words:- ", "-".join(scrabble.letters))
            user_word = input("\n Please use the Given letters : ")
        if scrabble.quit_game(user_word):
            break
        print("Your current score ", scrabble.user_score)

    print("\n" * 5 + " Hopefully you had a fun game: your final score is " + str(scrabble.user_score))
    break
