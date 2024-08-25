#import 'numpy'
import numpy as np

# 1-D Array to 2-D Array

#Create An 1-D Array
arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1)
print(arr1.shape)
print(arr1.ndim)

#Reshape the array in (3,3)
new_arr1 = arr1.reshape(3,3)
print(new_arr1)
print(new_arr1.shape)
print(new_arr1.ndim)

#2-D Array to 3-D Array

#Create An 2-D Array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape)
print(arr2.ndim)

#Reshape the array in (1,2,3)
new_arr2 = arr2.reshape(1,2,3)
print(new_arr2)
print(new_arr2.shape)
print(new_arr2.ndim)

#3-D Array to 2-D Array

#Create An 3-D Array
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)
print(arr3.shape)
print(arr3.ndim)

#Reshape the array in (12,)
new_arr3 = arr3.reshape(12)
print(new_arr3)
print(new_arr3.shape)
print(new_arr3.ndim)

