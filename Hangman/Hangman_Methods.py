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

def user_input_check(char,guess_count):

    if char in inputted_words:
        print(char + "!! -: You have already used that letter :- !!")
    elif (char.isdigit()):
        print("Please give me a LETTER and not a NUMBER")
    else:
        print("WRONG LETTER")
        inputted_words.append(char)
        guess_count += 1
    return guess_count,inputted_words



def Hanging_Man(curr_lives):
    return HANGMANPICS[curr_lives]



print(HANGMANPICS[-1]+
      "welcome to HangMan")









