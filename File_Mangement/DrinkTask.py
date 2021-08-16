import os
import re

filepath = os.path.join(os.path.dirname(__file__))


###  write to the Drinks order file if the drink is in the menu file ###
###  print the  drinks order from the file ###
###  read from the Ordered file and calculate a reciept for the user ###


def doc_clean(file):
    dict = {}
    try:
        with open(file + "/Drink_Menu.txt") as drinks:
            orders = drinks.read()
            for i in orders.split():
                dict[re.search("[^:\d]+", i).group()] = int(re.search("\d+", i).group())
            drinks.close()
    except FileNotFoundError:
        print("File does not exist")
    return dict


#print(doc_clean(filepath))


def Order_drink(file, drink):
    res = 0
    try:
        with open(file + "/Drink_Menu.txt") as drinks:
            orders = drinks.read()
            # print(re.search("^Coffee",orders.split())) #
            for i in orders.split():
                ### print(drink,  re.search("[^:\d]+", i).group()) ###
                if drink == re.search("[^:\d]+", i).group():
                    add_to_order(file, drink+":"+re.search("\d+", i).group())
                    print(f"I have added your {drink} to your orders")
            ### elif(drink not in re.search("^"+drink, i).group()): ###
            ### print(f" {drink} is not ont the Menu") ###

            drinks.close()
    except FileNotFoundError:
        print("File does not exist")


def add_to_order(file, drink):
    try:
        with open(file + "/Drinks_order.txt", "a") as orders:
            orders.write(drink+ "\n")
    except FileNotFoundError:
        print("File does not exist")

def Show_receipt(file):
    res = 0
    print("Your receipt:")
    print("\t You ordered: ")
    try:
        with open(file + "/Drinks_order.txt","r") as orders:
            receipt= orders.read()
            for i in receipt.split():
                results = re.search("\d+", i).group()
                print("\t",re.search("[^:\d]+", i).group(),"£",results)
                res += int(results)
            print("Total:-"+"£ " + str(res))
            orders.close()
    except FileNotFoundError:
        print("File does not exist")

## read from ordered file
## remove drink from ordered file

def remove_Order(file,drink):
    not_removed=True
    i=0
    try:
        with open(file + "/Drinks_order.txt","r+") as orders:
            receipt = orders.read()
            array = receipt.split()
            for i in array:
                print("------",i)


    except FileNotFoundError:
        print("File does not exist")
    except AttributeError:
        print(f"Your {drink} Drink was not ordered")

Order_drink(filepath, 'Coffee')
Show_receipt(filepath)
remove_Order(filepath, 'Coffee')
Show_receipt(filepath)
#                match = re.search("^" + drink + ".+", i).group()

#                if drink == match[0:len(drink)]:
 #                   array.remove(match)
  ##                  orders.write("")
    ##                orders.write("\n".join(array))
      #              orders.close()
       #             break
        #        elif(len(array)==0):
         #           print("You have not ordered anything")
          #      else:
           #         print("Error")
