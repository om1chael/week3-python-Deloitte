class Car_Class:
    def __init__(self,curr_speed,Max_speed):
        self.__Current_Speed=curr_speed
        self.__max_speed=Max_speed

    def Get_MaxSpeed(self):
        return self.__max_speed
    def Get_CurrSpeed(self):
        return self.__Current_Speed

    def Acceleration(self,acc):
        state = self.__Current_Speed + acc
        if(state >= self.__max_speed):
            print("Error:-: Your Car isn't this Powerfull")
        else:
            self.__Current_Speed=state

    def Deceleration(self,decc):
        state=self.__Current_Speed-decc
        if(state<0):
            print("Error:-: Car Cannot be negative Speed")
        else:
            self.__Current_Speed =state


car=Car_Class(14,100)

print(__name__)
print(car.Get_CurrSpeed())

for i in range(10):
    car_break=car.Deceleration(i*10)
    print(car.Get_CurrSpeed(),i*10)