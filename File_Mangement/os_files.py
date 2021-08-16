import os
#print(os.curdir)
#print(os.path.dirname(__file__))
file=open("text.txt")
print(file.read(),"dd")
# strip()
#

savings =[100,200,300,400,500]
percent = lambda a:(a*0.1)+a

print(list(map(percent,savings)))


savings =[100,200,300,400,500]
bthen100 = lambda a:a==300,

#print(list(filter(bthen100,savings)))
filepath=os.path.join(os.path.dirname(__file__)+"/text.txt")
try:
    with open(filepath) as file:
        data = filepath
    print(data)
except FileNotFoundError as errmsg:
    print("Could Not Find")
    print(errmsg)

def Write_toFile(filepath,items):
    try:
        with open(filepath,"w") as file:
            file.write(items)
    except FileNotFoundError:
        print("Get the file ")
        raise

Write_toFile(filepath,"stake  \n")
