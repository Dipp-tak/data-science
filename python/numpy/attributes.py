#Import the 'numpy' library for use with the rest of the code.
import numpy as np

#Create An Array using 'numpy'
arr = np.array([1,2,3,4,5])

#Print the Array
print("The Array is : ",arr)

#Print the type of the Array
print("Type of Array: ",type(arr))

#Print the dimension of the Array
print("Dimension of the Array is : ",arr.ndim)

#Print the shape of the Array
print("The shape of the Array is : ",arr.shape)

#Print the data type of the Array
print("Data type of the Array is : ",arr.dtype)

#Print the size of the Array
print("Size of The Array is : ",arr.size)

#Print the itemsize of the Array
print("Size of Array element : ",arr.size)

#Print the total size of the Array
print("Array Space in Bytes : ",arr.nbytes)
