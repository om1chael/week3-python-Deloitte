from Hangman_words import word_list,HANGMANPICS
from random import randint

inputted_words=[]
guess_count=0

def random_word():
    index = randint(0,len(word_list))
    return word_list[index]

def word_filler(char,correct_words,random_word):
    if char in random_word:
        print("!! Letter FOUND !!")
        for i in range(len(random_word)):
            if (char == random_word[i]):
                correct_words[i] = random_word[i]
    return correct_words

def user_input_check(char,guess_count,rand_word):

    if char in inputted_words:
        print(char + "!! -: You have already used that letter :- !!")
    elif (char.isdigit()):
        print("Please give me a LETTER and not a NUMBER")
    elif(char not in rand_word):
        print(" ######---> WRONG LETTER <---####")
        inputted_words.append(char)
        guess_count += 1
    else:
        pass
    return guess_count,inputted_words

world_names={
"judas": {'Date': "30AD", "Text": "Was the pieces of silver worth loosing the hangman "},
"chester": {'Date': 2017, "Text": "Tried soo hard and got soo far, but in the end you lost the hangman"},
"louis": {'Date': 1983, "Text": "louis -'It is legal because I wish it.', this is why you were guillotined "},
"hideki": {'Date': 1948, "Text": "hideki-'FOR THE EMPERORRR'- okay, we get it you love your senpai "}
}


def Hanging_Man(curr_lives):
    return HANGMANPICS[curr_lives]

hangman_img="    "+HANGMANPICS[-1]

print("\t"+str(hangman_img) +
"#################################### \n"+
      "\t    Welcome to HangMan \n"+
"####### WORLD HISTORY DLC #########")
