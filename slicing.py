numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print("Original List:", numbers) # Original List: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
# slicing from index 2 to 5
numbers_slice = numbers[2:5]
print("Sliced List from index 2 to 5:", numbers_slice) # Sliced List from index 2 to 5: [2, 3, 4]   

print("Original List:", numbers) # Original List: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    

numbers_slice = numbers[5:2:-1]
print("Sliced List from index 5 to 2 in reverse order:", numbers_slice) # Sliced List from index 5 to 2 in reverse order: [5, 4, 3]

numbers_slice = numbers[-5:-2]
print("Sliced List from index -5 to -2:", numbers_slice) # Sliced List from index -5 to -2: [5, 6, 7]


numbers_slice = numbers[::2]
print("Sliced List with step 2:", numbers_slice) # Sliced List with step 2: [0, 2, 4, 6, 8] 

numbers_slice = numbers[1:8:2]
print("Sliced List from index 1 to 8 with step 2:", numbers_slice) # Sliced List from index 1 to 8 with step 2: [1, 3, 5, 7]    

text = "Hello, World"
substring = text[7:12]
print("Substring from index 7 to 12:", substring) # Substring from index 7 to 12: World

substring = text[12:7:-1]
print("Substring from index 12 to 7 in reverse order:", substring) # Substring from index 12 to 7 in reverse order: dlroW   

substring = text[::2]
print("Substring with step 2:", substring) # Substring with step 2: Hlo ol  

substring = text[7:]
print("Substring from index 7 to the end:", substring) # Substring from index 7 to the end: World  

substring = text[:5]
print("Substring from the start to index 5:", substring) # Substring from the start to index 5: Hello

