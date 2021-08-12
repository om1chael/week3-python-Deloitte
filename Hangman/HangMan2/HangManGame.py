import Hangman_Methods
On_Menu = True
while(On_Menu):
    Hangman_game = Hangman_Methods.Game()
    start_game = input("\n Do you want to play yes/no ?:- ")
    if(start_game == "no"):
        break
    name = input("\n What is your name:- ")
    Hangman_game.set_name(name)
    print(f" \n !! Hello {name} Lets Play !!")

    while(Hangman_game.EndGame_conditions()):
        if (Hangman_game.DLC(name)):
            break

        print(" You Have Lives :- "+str(Hangman_game.lives))
        user_input = input("\n Give me your First letter:- ")
        print(Hangman_game.Hangman_ASCII(Hangman_game.lives))
        print("\n User Guess:-: ", Hangman_game.Random_word,Hangman_game.Check_User(user_input))

    print(Hangman_game.Game_Response+"  "+Hangman_game.Name )






