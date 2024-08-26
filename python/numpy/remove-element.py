#Removeing element from Array

#Import 'numpy'
import numpy as np

#Create An Array
arr = np.array([1,2,3,4,5,6,7,8,9])
print("The Array is: ",arr)

# I want to remove element 2,4 & 8 from the Array, the index of 2,4,8 is 1,3,7 so removing the element using the their index
new_arr = np.delete(arr,[1,3,7])
print("Ater deleting element the new Array is : ",new_arr)
