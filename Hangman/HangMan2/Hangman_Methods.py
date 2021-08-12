from Hangman_words import word_list,HANGMANPICS,world_names
import random

class Game:
    def __init__(self):
        self.Name = ""
        self.Random_word = self.Generate_word().lower()
        self.lives = 6
        self.used_letters=[]
        self.lines = ["-"]*len(self.Random_word)
        self.Game_Response = ""

    def set_name(self, name):
        self.Name = name


    def DLC(self,name):
        if (name in world_names.keys()):
            info = world_names[name]
            self.Game_Response += str(info["Date"]) + "-" + info["Text"]
            return True

    def Generate_word(self):
        return random.choice(word_list)

    def Hangman_ASCII(self,index):
        return HANGMANPICS[len(HANGMANPICS)-index]

    def Check_User(self,user_input):
        random_word=" ".join(self.Random_word)
        for i in range(len(self.Random_word)):
            if(user_input == random_word.split()[i]):
                self.lines[i]=user_input
        self.Wrong_Answer(user_input)
        return "".join(self.lines)

    def Wrong_Answer(self,user_input):
        if user_input not in self.Random_word and user_input not in self.used_letters:
            print("##:- Wrong Letter -:## "+ user_input)
            self.used_letters.append(user_input)
            self.lives-=1
        print("##:- Used Letters -:##", self.used_letters)

    def EndGame_conditions(self):
        fun="Hopefull you had a Fun"
        if(self.lives == 0):
            self.Game_Response += "\n ### GameOver -- You Lost He was HUNG  ###  "+fun
            return False
        elif("".join(self.lines) == "".join(self.Random_word)):
            self.Game_Response += "\n\n ##### WellDone -- You Won the Game #### "+fun
            return False
        else:
            return True


















hangman_img = HANGMANPICS[-1]

print("\t" + str(hangman_img) +
      "#################################### \n" +
      "\t    Welcome to HangMan \n" +
      "####### WORLD HISTORY DLC #########")

