import numpy as np

# how to create an array
array1 = np.array([1,2,3,4])
print(array1)  # [1 2 3 4]
print(type(array1))  # <class 'numpy.ndarray'>

myList = [1,2,3,4,5]
myArray = np.array(myList)
print(myArray)
print(type(myArray))

# properties associated with numpy array
print("Array 1 , Dimension : ", array1.ndim) # 1
print("Array 1 , shape : ", array1.shape) # (4,)
print("Array 1 , size : ", array1.size) # 4
print("Array 1 , data type : ", array1.dtype) # int64

array2 = np.array([
            [1,2,3,4,5],
            [6,7,8,9,10]
        ])

print("Array 2 , Dimension : ", array2.ndim) # 2
print("Array 2 , shape : ", array2.shape) # (2, 5)
print("Array 2 , size : ", array2.size) # 10
print("Array 2 , data type : ", array2.dtype) # int64

array3 = np.array([
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]
        ])
print("Array 3 , shape : ", array3.shape) # (3, 5)
#Array reshaping
print("After reshaping - 3/5 to 5/3 \n")
print(array3.reshape(5,3))
 #[[ 1  2  3]
 #[ 4  5  6]
 #[ 7  8  9]
 #[10 11 12]
 #[13 14 15]]

print(array3.reshape(15,1))
print(array3.reshape(1,15))
print(array3.reshape(15,-1)) # here -1 is undefined and decided by numpy based on the number of elements in an array
#print(array3.reshape(-1,-1)) #ValueError: can only specify one unknown dimension
print(array3.reshape(-1,)) # flatten [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
print(array3.flatten()) # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
#print(array3.reshape(5,2)) # ValueError: cannot reshape array of size 15 into shape (5,2)

## Indexing and slicing - it is same as of python list
print("####################################")
data = np.array([1,2,3,4,5])
print(data) # [1 2 3 4 5]
print(data[0:2]) # [1 2]
print(data[1:]) # [2 3 4 5]
print(data[:1]) #  [1]
print(data[-1]) # 5
print(data[-2]) # 4

############ create special arrays 
print("########################")

print("An arrray of zeros of size 10 : \n")
print(np.zeros(10, dtype=np.int64)) # [0 0 0 0 0 0 0 0 0 0]
print("An arrray of zeros of size 5 X 4 : \n")
print(np.zeros(shape = (5,4)))

print("An arrray of ones of size 3 X 4 : \n")
print(np.ones(shape = (3,4)))

print("create a full matrix for given value : \n")
print(np.full((3,4), 7))

print("Identity matrix of size 4 X 4 : \n")
print(np.eye(4))

print("create a diagonal matrix from 1d array: \n")
print(np.diag([1,2,3,4]))

my_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("The array : \n\n", my_array)
print()
print("The diagonal of the array : ", np.diagonal(my_array))
print()
print("Trace of the array : ", np.trace(my_array))

print("matrix with random numbers between 0 and 1 of size 3x3 : \n")
print(np.random.rand(3,3))

print("matrix with random integers between 1 and 10 of size 4x4 : \n")
print(np.random.randint(1,10,(4,4)))

print("An array from 2 to 50 with step size 3 :\n")
print(np.arange(2,50,3)) # [ 2  5  8 11 14 17 20 23 26 29 32 35 38 41 44 47]

print("An array linearly distributed from 0 to 10 in 5 partitions : \n")
print(np.linspace(0,10,num=5))


array_4 = np.array([2,1,5,10,19,12,8,15])
print("Original array : ")
print(array_4)

print("Sorted array : ")
print(np.sort(array_4))

print("Original array : ")
print(array_4)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])
print("Array 1 :\n")
print(x)
print("Array 2 :\n")
print(y)

print("Concatenated arrays : \n")
print(np.concatenate((x,y), axis = 0)) 

arr1 = np.array([1,2,3]).reshape(1,3)
arr2 = np.array([4,5,6]).reshape(1,3)
print(arr1)
print(arr1.shape)
print()
print(arr2)
print(arr2.shape)
print()

# Basic Array operations
array_5 = np.array([1,2])
array_6 = np.ones(2,dtype=int)
print("Array 5 : ", array_5)
print("Array 6 : ", array_6)

print(f" Array Addition : {array_5} + {array_6} : ", array_5 + array_6)
print(f" Array Subraction : {array_5} - {array_6} : ", array_5 - array_6)
print(f" Array (Element-wise) Multiplication : {array_5} * {array_6} :", array_5 * array_6)

array_7 = np.arange(-4, 10, 2)
print("Define new array : ", array_7)
print("sum of the elements : ", array_7.sum())
print("Min of the elements : ", array_7.min())
print("Max of the elements : ", array_7.max())
print("Mean of the elements : ", array_7.mean())
print("Mean of the elements : ", np.mean(array_7))


#Broadcasting
arr_1d = np.array([1,2,3,4])
scalar = 5
print(f"(1) {arr_1d} + {scalar}", arr_1d + scalar)
print(f"\n (2) {scalar} + {arr_1d}", scalar + arr_1d)

arr_1d = np.array([1,3,5,9])
scalar = 1.4
print(f"(1) {arr_1d} * {scalar}", arr_1d * scalar)
print(f"\n (2) {scalar} + {arr_1d}", scalar * arr_1d)

arr_2d = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
arr_1d = np.array([1,2,3])
print(f"(1) {arr_2d}\n\n + \n\n {arr_1d} = \n\n {arr_2d + arr_1d} ")

arr_2d = np.array([[1,2,3] , [4,5,6] , [7,8,9]])
arr_1d = np.array([[1],[2],[3]])
print(f"(1) {arr_2d}\n\n + \n\n {arr_1d}", arr_2d + arr_1d)

######### Filtering in NumPy
print("++++++++++++++++++++++++++++++++++++++++++++")
array_9 = np.array([[10,12,8,4],[1,2,25,7]])
print(array_9)

condition1 = (array_9 > 20) 
print("Condition imposed on the array gives : \n")
print(condition1) #masked
print("Filtered array : \n", array_9[condition1])
print("Filtered array : \n", array_9[array_9 > 20])
#array_9[array_9 > 10] = 10
#print("Modified array : \n", array_9)

condition1 = (array_9 >=10)
condition2 = (array_9 <=30)
print("Elements with both conditions : ", array_9[condition1 & condition2])
print("Elements with either of conditions : ", array_9[condition1 | condition2])

data = np.array(
    [
        [10,5,20],
        [25,15,30],
        [35,25,40],
        [45,35,50]        
    ]
)
condition = data[:,0] > 20 # data[:,0] --> meaning (:) all the rows, (0) first column
filtered_data = data[condition]
print("Keep only those rows with elements greater than 20 in column 1 : \n")
print(filtered_data)

#save and load Numpy data
array_10 = np.array([[10,12,8,4],[1,2,25,7]])
print("define a new 2d array : \n")
print(array_10)

np.save('array_10', array_10) # will be saved by name array_10.npy
new_array = np.load('array_10.npy')
print("loaded array : \n\n", new_array)

np.savetxt('array_10_csv.csv ', array_10) # will be saved by name array_10_csv.csv

new_array = np.loadtxt('array_10_csv.csv')
print("loaded array : \n\n", new_array)
