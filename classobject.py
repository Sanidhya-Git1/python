class Dog: 

    #define a constructor
    def __init__(self, name, age, wt):
        self.name = name
        self.age = age
        self.wt = wt
        print("created a new Dog object : " + name)

    #define a destructor
    def __del__(self):
        print("deleting this object : "+self.name)

    # change default repr -> representation
    def __repr__(self):
        return "name : " + self.name + " wt : "+str(self.wt)

    #Define method
    def walk(self):
        print("I am waliking : "+self.name)

dog1 = Dog("Sky", 12, 5)
print(dog1)
print(dog1.name)
print(dog1.age)
print(dog1.wt)

#defining more attribute to a class
dog1.ht = 6
print(dog1.ht)
print(dog1)

def fun(dog : Dog):
    print(dog.name)
    dog.name = "xyz"
    print(dog.name)

#fun(dog1) 

#del dog1
print(dog1)