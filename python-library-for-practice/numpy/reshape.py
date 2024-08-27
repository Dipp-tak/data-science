#import 'numpy'
import numpy as np

# 1-D Array to 2-D Array
print("\n1-D to 2-D Array Conversation \n")

#Create An 1-D Array
arr1 = np.array([1,2,3,4,5,6,7,8,9])
print("1-D Array: ",arr1)
print("Shape of 1-D Array:",arr1.shape)
print("The dimenson of 1-D Array:",arr1.ndim,"\n")

#Reshape the array in (3,3)
new_arr1 = arr1.reshape(3,3)
print("Convert Array's: \n",new_arr1)
print("Convert Array's shape: ",new_arr1.shape)
print("Convert Array's Dimenson: ",new_arr1.ndim) 

#2-D Array to 3-D Array
print("\n2-D to 3-D Array Conversation \n")

#Create An 2-D Array
arr2 = np.array([[1,2,3],[4,5,6]])
print("2-D Array: \n",arr2)
print("Shape of 2-D Array:",arr2.shape)
print("The dimenson of 2-D Array:",arr2.ndim,"\n")


#Reshape the array in (1,2,3)
new_arr2 = arr2.reshape(1,2,3)
print("Convert Array's: \n",new_arr2)
print("Convert Array's shape: ",new_arr2.shape)
print("Convert Array's Dimenson: ",new_arr2.ndim) 


#3-D Array to 2-D Array
print("\n3-D to 1-D Array Conversation \n")

#Create An 3-D Array
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("3-D Array: \n",arr3)
print("Shape of 3-D Array:",arr3.shape)
print("The dimenson of 3-D Array:",arr3.ndim,"\n")

#Reshape the array in (12,)
new_arr3 = arr3.reshape(12)
print("Convert Array's: \n",new_arr3)
print("Convert Array's shape: ",new_arr3.shape)
print("Convert Array's Dimenson: ",new_arr3.ndim)

