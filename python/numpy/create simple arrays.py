#Import 'numpy'
import numpy as np

#Create An Array with the element 0.
zero_arr = np.zeros((5))
#Print the Array
print("The Array With Element Zero : \n",zero_arr)

#Create An Array with the element 1.
one_arr = np.ones((7))
#Print the Array
print("The Array With Element one : \n",one_arr)

#Create An Array with empty() function.
empty_arr = np.empty((2))
#Print the Array
print("The Array With empty() function : \n",empty_arr)

#Create An Array with range() function.
rang_arr = np.arange(4)
#Print the Array
print("The Array With range() function : \n",rang_arr)

#Create An Array with linspace() function.
linespace_arr = np.linspace(0,10,num=5)
#Print the Array
print("The Array With linspace() function : \n",linespace_arr)

#Create An Array of even number.
even_arr = np.arange(2,20,2)
#Print the Array
print("Even numbers Arry 0 to 20 : \n",even_arr)

#Create An Array of odd number.
odd_arr = np.arange(1,20,2)
#Print the Array
print("Odd Numbers Array 0 to 20 : \n",odd_arr)
