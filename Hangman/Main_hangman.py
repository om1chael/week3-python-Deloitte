import Hangman_Methods
import os
Menu_state=True
Game_not_over=True
random_word=Hangman_Methods.random_word().lower()
guess_count=0
text=""
correct_words=["-"]*len(random_word)

## the menu state
while Menu_state:
    start = input("Do you want to play Hangman yes/no ? ")
    name=input("Name Please:- ")
    if(name in Hangman_Methods.world_names.keys()):
        info=Hangman_Methods.world_names[name]
        text+=str(info["Date"])+"-"+info["Text"]
        break
    else:
        pass

    print("Hello User:-: "+name)

## if user wants to play the game
    if start=="yes":
        while Game_not_over:
            char = input("Give Me A Letter:- ")
            print("\n\n\n" *20)
            print("Lives Left:-"+str(6-guess_count))

## Checks if the inputted letter exists in the senetnce
            correct_words=Hangman_Methods.word_filler(char,correct_words,random_word)
            guess_count,inputted_words=Hangman_Methods.user_input_check(char,guess_count,random_word)

## shows user a list of used words
            print("Used Letters:- ", inputted_words)

## the winning/loosing constraints
            if(guess_count>=7):
                print("Sorry you have lost the Game: Correct word was:-> "+random_word)
                break
            elif("".join(correct_words)==random_word):
                text+="Hopefully you had Fun Bye:- "
                print("<<---------------- Well Done You Did it ------------------------>>")
                break

## Show hangman GUI
            print(Hangman_Methods.Hanging_Man(guess_count))
            print("Guessing word:-:"+"".join(correct_words))

### if user doesnt want to play the game
    elif(start=="no"):
        still_alive=False
        break
    else:
        print("I dont understand")
## Ending message

print(text+"<--- You lost --->" + name)



