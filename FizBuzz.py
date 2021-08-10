def FizzBuzz(n):

    for i in range(n):
        if(i%(5*3) == 0 ):
            print("FizBuzz")
        elif(i%5 == 0):
            print("Buzz")
        elif(i%3==0):
            print("Fizz")
        else:
            print(i)


