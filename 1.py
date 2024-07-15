# Numpy is the core library for scientific and numeric computing in Python.
#Provides high-performance multidimensional array object and tools for working with arrays

#NumPy is usually imported under the np alias
import numpy as np

#create a numpy array
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr[2])
#array object in numpy is called ndarray

#NumPy is faster than lists because NumPy arrays are stored one continuous place in memory unlike lists so processes can access and manipulate them very easily.



#Dimensions in arrays
#A dimension in arrays is one level of array depth (nested arrays).
#0-D Arrays or Scalars -> are elements in an array
a = np.array(42) #0
print(a.ndim) #returns dimension of array
#1-D Arrays (has 0-D arrays as its elements)
b = np.array([1,2,3,4,5])
print(b.ndim) #1
#2-D Arrays (has 1-D arrays at its elements)
c = np.array([[1,2,3],[4,5,6]])
print(c[0,1]) #2
print(c.ndim) #2
#3-D Arrays (has 2-D arrays as its elements)
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d.ndim) #3
print(d[0,1,2]) #6
#Higher Dimensional Arrays
#When the array is created, you can define the number of dimensions by using the ndmin argument.
e = np.array([1,2,3,4], ndmin = 5)
print(e.ndim) #5
#In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

#Use negative indexing to access an array from the end.



#Slicing Arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2 3 4 5]
#The result includes the start index, but excludes the end index.
#Negative Slicing
print(arr[-3,-1]) #[5 6]
#Step Value
print(arr[1:5:2]) #[2 4]
print(arr[::2]) #return every other element from the entire array

#Slicing 2-D arrays
arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 1:4]) #[7 8 9]
#From both elements, return index 2:
print(arr[0:2, 2]) #[3 8]
#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4]) #[[2 3 4][7 8 9]]










