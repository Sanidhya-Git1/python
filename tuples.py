fruits = ("apple", "banana", "cherry") 
print("Fruits Tuple:", fruits); #Fruits Tuple: ('apple', 'banana', 'cherry')   

first_fruit = fruits[0]; #Accessing an element in a tuple
print("First Fruit:", first_fruit); #First Fruit: apple

# Tuple is immutable - cannot add, remove or change elements in a tuple
#fruits.append("orange"); # AttributeError: 'tuple' object has no attribute 'append'
#fruits.remove("banana"); # AttributeError: 'tuple' object has no attribute 'remove'
#fruits[1] = "kiwi"; # TypeError: 'tuple' object does not support item assignment    

mixed_tuple = ("apple", 42,3.14,(1,2,3))
print("Mixed Tuple:", mixed_tuple); # Mixed Tuple: ('apple', 42, 3.14, (1, 2, 3))


