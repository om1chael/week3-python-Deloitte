class Shopping_cart:
    def __init__(self):
        self.basket=[]
    def add(self,item):
        self.basket.append(item)
    def show_basket(self):
        return self.basket

    def return_total(self):
        total=0
        for products in self.basket:

            total=total+products.price
        print(f"Total :{total}")

class product:
    def __init__(self,price,name,brand):
        self.price = price
        self.name =name
        self.brand =brand


aldi=Shopping_cart()
milk=product(1.23,"Milk","Aldi")
beef=product(3.23,"Beef","Aldi")

aldi.add(milk)
aldi.add(beef)



aldi.return_total()







