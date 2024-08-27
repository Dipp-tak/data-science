#Adding element in Array

#Import 'numpy'
import numpy as np

#Create An Array
arr = np.array([1,2,3,4,5,7,8,9])
print("The Array is : ",arr)

# I want to add number 6 at the fifth index after 5 and before 7

#new_arr = np.insert(old array name,index,element)
new_arr = np.insert(arr,5,6)
print("After Inserting element 6 at index 5 the new Array is : ",new_arr)
