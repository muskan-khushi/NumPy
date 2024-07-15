# Numpy is the core library for scientific and numeric computing in Python.
#Provides high-performance multidimensional array object and tools for working with arrays

#NumPy is usually imported under the np alias
import numpy as np

# #create a numpy array
# #To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))
# print(arr[2])
# #array object in numpy is called ndarray

# #NumPy is faster than lists because NumPy arrays are stored one continuous place in memory unlike lists so processes can access and manipulate them very easily.



# #Dimensions in arrays
# #A dimension in arrays is one level of array depth (nested arrays).
# #0-D Arrays or Scalars -> are elements in an array
# a = np.array(42) #0
# print(a.ndim) #returns dimension of array
# #1-D Arrays (has 0-D arrays as its elements)
# b = np.array([1,2,3,4,5])
# print(b.ndim) #1
# #2-D Arrays (has 1-D arrays at its elements)
# c = np.array([[1,2,3],[4,5,6]])
# print(c[0,1]) #2
# print(c.ndim) #2
# #3-D Arrays (has 2-D arrays as its elements)
# d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(d.ndim) #3
# print(d[0,1,2]) #6
# #Higher Dimensional Arrays
# #When the array is created, you can define the number of dimensions by using the ndmin argument.
# e = np.array([1,2,3,4], ndmin = 5)
# print(e.ndim) #5
# #In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

# #Use negative indexing to access an array from the end.



# #Slicing Arrays
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5]) #[2 3 4 5]
# #The result includes the start index, but excludes the end index.
# #Negative Slicing
# print(arr[-3:-1]) #[5 6]
# #Step Value
# print(arr[1:5:2]) #[2 4]
# print(arr[::2]) #return every other element from the entire array

# #Slicing 2-D arrays
# arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr1[1, 1:4]) #[7 8 9]
# #From both elements, return index 2:
# print(arr1[0:2, 2]) #[3 8]
# #From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
# print(arr1[0:2, 1:4]) #[[2 3 4][7 8 9]]


# #Data Types
# # i - integer
# # b - boolean
# # u - unsigned integer
# # f - float
# # c - complex float
# # m - timedelta
# # M - datetime
# # O - object
# # S - string
# # U - unicode string
# # V - fixed chunk of memory for other type ( void )
# arr = np.array([1,2,3,4,5,6,7])
# print(arr.dtype) #int32
# arr = np.array(["apple", "banana", "mango"])
# print(arr.dtype) #<U6

# #Creating array with defined data types
# arr = np.array([1,2,3,4], dtype='S')
# print(arr.dtype) #|S1
# #for i, u, f, S and U we can define size as well.
# #create an array with data type 4 bytes integer
# arr = np.array([1,2,3,4], dtype='i4')
# print(arr.dtype) #int32

# #A non integer string like 'a' can not be converted to integer (will raise an error)

# #Converting Data type on existing  arrays
# #best way -> make a copy of the array with astype() method.
# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# print(newarr) #[1 2 3]
# print(newarr.dtype) #int32



# #NumPy Array Copy vs View
# # The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# # The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# # The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# #Make a copy, change the original array, and display both arrays:
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)
# #Make a view, change the original array, and display both arrays:
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)
# #make a view, change the view and display both arrays
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[0] = 31
# print(arr)
# print(x)

# #check if array owns data
# #Every NumPy array has the attribute base that returns None if the array owns the data.
# #otherwise, the base attribute refers to the original object
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# y = arr.view()
# print(x.base) #None
# print(y.base) #[1 2 3 4 5]



# #NumPy Array Shape
# #The shape of an array is the number of elements in each dimension.
# #NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr.shape) #(2, 5)
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr.shape) #(1,1,1,1,4)



# #NumPy Array Reshape
# #1D to 2D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3) #outermost dimension will have 4 arrays, each with 3 elements
# print(newarr)
# #1D to 3D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2,3,2) #outermost dim will have 2 arrays, which will have 3 arrays each with 2 elements each.
# print(newarr)
# #We can reshape into any shape as long as the elements required for reshaping are equal in both shapes.
# #returned array is a view
# #Unknown Dimension
# # allowed to have one "unknown" dimension.
# # Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2, 2, -1)
# print(newarr)
# # We can not pass -1 to more than one dimension.



















