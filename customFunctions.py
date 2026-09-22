numbers = [4,2,9,1,5]

print(sorted(numbers)) # [1, 2, 4, 5, 9]
print(numbers) # [4, 2, 9, 1, 5]

#print(numbers.sort()) # None
#print(numbers) # [1, 2, 4, 5, 9]

# sort() - it changes in place 
# sorted() - returns a new list


# words = ["apple", "banana", "cherry", "date", "fig"]
# sorted_words = sorted(words, key = len , reverse = True)
# print(sorted_words) # ['banana', 'cherry', 'apple', 'date', 'fig']
# print(words) # ['apple', 'banana', 'cherry', 'date', 'fig']

# sorted_words = sorted(words, key = lambda x : x[1] , reverse = False)
# print(sorted_words) # ['banana', 'date', 'cherry', 'fig', 'apple']
# print(words)

points = [[1,2],[0,4],[6,3],[1,3]]
# sort this array based on both the first and second elements

# sort this array based on both the first element
sorted_points = sorted(points, key = lambda x : x[0])
print(sorted_points) # [[0, 4], [1, 2], [1, 3], [6, 3]]
# sort this array based on both the second element
sorted_points = sorted(points, key = lambda x : x[1])
print(sorted_points) #[[1, 2], [6, 3], [1, 3], [0, 4]]
