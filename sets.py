fruits =  {"apple", "banana", "cherry", "apple"}; #Set with duplicate element "apple"
print("Fruits Set:", fruits); #Fruits Set: {'banana', 'cherry', 'apple'} - Duplicate element "apple" is removed, it is unordered

# mutable collection
fruits.add("orange"); #Adding an element to the set
print("Fruits Set after adding 'orange':", fruits); #Fruits Set after adding

fruits.remove("banana"); #Removing an element from the set
print("Fruits Set after removing 'banana':", fruits); #Fruits Set after removing 'banana': {'cherry', 'apple', 'orange'}

#fruits[0] = "kiwi"; #TypeError: 'set' object does not support item assignment - Sets are unordered, cannot access elements by index


mixed_set = {"apple", 42, 3.14, (1, 2, 3)}
print("Mixed Set:", mixed_set); # Mixed Set: {42, 3.14, (1, 2, 3), 'apple'} - Sets can contain different data types, but they are unordered

#mixed_set = {"apple", 42, 3.14, (1, 2, 3), [1,2,3]} #TypeError: unhashable type: 'list' - Sets cannot contain mutable elements like lists or dictionaries 
#mixed_set = {"apple", 42, 3.14, (1, 2, 3), [1,2,3], {"name": "sanidhya"}} #TypeError: unhashable type: 'dict' - Sets cannot contain mutable elements like lists or dictionaries 