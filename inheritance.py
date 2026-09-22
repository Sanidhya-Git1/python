class Book: 
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book : {self.title}, Quantity : {self.quantity} , Author : {self.author} , Price : {self.__price} "

class Novel (Book) : 
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

class Academic (Book): 
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch


novel1 = Novel('2 states', 20, 'Matt', 200 , 187)
novel1.set_discount(0.0)

academic1 = Academic('Python foundations', 12, 'PSF', 655 , 'IT')

print(novel1)
print(academic1)


# python supports multiple inheritance too
class Bird : 
    def fly(self):
        print("I can fly")

class Fish:
    def swim(self):
        print("I can swim")

class FlyingFish(Bird, Fish): # multiple inheritance
    pass

ff = FlyingFish()
ff.fly()
ff.swim()