#Import 'numpy'
import numpy as np

#Create Arrays
arr1 = np.array([5,6,7,8,9])
arr2 = np.array([1,2,3,4])

#Print the creating Arrys
print("The 1st Array is : ",arr1)
print("The 2nd Array is : ",arr2)

#Concatenate arr1 & arr2
arr  = np.concatenate((arr1,arr2))
#Print the final Array
print("After the Concatenation of 1st and 2nd Array, the final Array is : ",arr)
