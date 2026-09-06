intList =  [1, 2, 3, 4, 5]; 
mixed_list = [1, "two", 3.0, True, None];
mixed_list_diffData_types = [1, "two", 3.0, True, None, [1, 2], {"name": "sanidhya"}, (1, 2), {1, 2}];

print("Integer List:", intList); #Integer List: [1, 2, 3, 4, 5]
print("Mixed List:", mixed_list); #Mixed List: [1, 'two', 3.0, True, None]
print("Mixed List with Different Data Types:", mixed_list_diffData_types); #Mixed List with Different Data Types: [1, 'two', 3.0, True, None, [1, 2], {'name': 'sanidhya'}, (1, 2), {1, 2}]

fruits = ["apple", "banana", "cherry"];
print("Fruits List:", fruits); #Fruits List: ['apple', 'banana', 'cherry']

# mutable - add, remove or change elements in a list
# adding in a list
fruits.append("orange"); #Adding an element to the list
print   ("Fruits List after appending 'orange':", fruits); #Fruits List after appending 'orange': ['apple', 'banana', 'cherry', 'orange']   

#removing from a list
fruits.remove("banana"); #Removing an element from the list
print("Fruits List after removing 'banana':", fruits); #Fruits List after removing 'banana': ['apple', 'cherry', 'orange']

# changing an element in a list
fruits[1] = "kiwi"; #Changing an element in the list
print("Fruits List after changing 'cherry' to 'kiwi':", fruits); #Fruits List after changing 'cherry' to 'kiwi': ['apple', 'kiwi', 'orange']


