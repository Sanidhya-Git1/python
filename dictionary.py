student_ages = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 21,
    "Alice": 22,  # Duplicate key, will overwrite previous value
}
print(student_ages)  # Output: {'Alice': 22, 'Bob': 22, 'Charlie': 21}

# accessing values using keys
print("Age of Alice:", student_ages["Alice"])  # Output: 22
print("Age of Bob:", student_ages["Bob"])    # Output: 22
print("Age of Charlie:", student_ages["Charlie"]) # Output: 21 

# adding a new key-value pair
student_ages["David"] = 23
print("Updated student ages:", student_ages)  # Output: {'Alice': 22, 'Bob': 22, 'Charlie': 21, 'David': 23}    

# modifying an existing value
student_ages["Bob"] = 23
print("Updated student ages after modifying Bob's age:", student_ages)  # Output:


#different data types as keys and values
# keys must be immutable types (like strings, numbers, or tuples), while values can be of any type (including lists, dictionaries, etc.)
mixed_dict = {
    "name": "Alice",
    42: "answer",
    (1, 2): "coordinates"
}


print("Mixed dictionary:", mixed_dict)  # Output: {'name': 'Alice', 42: 'answer', (1, 2): 'coordinates'}    
print(mixed_dict['name'])  # Output: Alice
print(mixed_dict["name"])  # Output: Alice
print(mixed_dict[42])  # Output: answer

mixed_dict_1 = {
    'name': 'Alice',
    42: 'answer',
    (1, 2): "coordinates"
} 
print("Mixed dictionary 1:", mixed_dict_1)  # Output: {'name': 'Alice', 42: 'answer', (1, 2): 'coordinates'}


cities = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (51.5074, -0.1278): "London"
}

print("Cities dictionary:", cities)  # Output: {(40.7128, -74.0060): 'New York', (34.0522, -118.2437): 'Los Angeles', (51.5074, -0.1278): 'London'}

#  Access a value using a tuple key
print(cities[(40.7128, -74.0060)])   # Output: New York

nyc_coords = (40.7128, -74.0060)
print(cities[nyc_coords])  # Output: New York

# Add a new tuple key-value pair
cities[(35.6764, 139.6500)] = "Tokyo"
print("Updated cities dictionary:", cities)  # Output: {(40.7128, -74.0060): 'New York', (34.0522, -118.2437): 'Los Angeles', (51.5074, -0.1278): 'London', (35.6764, 139.6500): 'Tokyo'}   

