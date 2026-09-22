class Car : 
    wheels = 4 #public attribute
    _color = "red"   # protected attribute
    __engine = "V8"  # private attribute


class MyClass: 
    def __init__(self):
        self.public_attribute = 42
        self._protected_attribute = 50
        self.__private_attribute = 55

    def public_method(self):
        return "This is a public method"

    def _protected_method(self):
        return "This is a protected method"

    def __private_method(self):
            return "This is a protected method"

obj = MyClass()
print(obj.public_attribute) # Accessing a public attribute 
print(obj.public_method())  # Accessing a public method 
print(obj._protected_attribute)  # Accessing a protected attribute (not recommended)
print(obj._protected_method())  # Accessing a protected method  (not recommended)

#print(obj.__private_attribute)  # Error 
#print(obj.__private_method())  # Error

