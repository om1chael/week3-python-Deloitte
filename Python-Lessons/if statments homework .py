#######list of movies with d
movies = {"Spiderman": {'release Date': 2002,  "rating":"PG"},
          "shrek": {'release Date': 2001,  "rating":"PG-13"},
          "mission impossible": {'release Date': 1996,"rating":"PG-13"},
          }

####### print the list of movies ###
print("movie list",movies.keys())
#### ask the user for input ###
movie=input("what movie do you want see from the list \n")
### make sure that the movie is within the list ###
while(movie not in movies.keys()):
    print("Try again, movie does not exist")
    movie = input("what movie do you want see from the list \n")

### another validatted input ###

valid=True
while valid:
    age = input("give me your age:- ")
    if(age.isdigit()):
        age = int(age)
        valid=False
    else:
        print("try again mate")

## the if section ##
statment= f"you can watch {movie}. Rated:{movies[movie]['rating']}. have a fun time"

if movies[movie]["rating"] == "PG" and int(age)> 10:
    print(statment)
elif movies[movie]["rating"] == "PG-13" and int(age) > 13:
    print(statment)
else:
    print("try again mate, you are too young")
