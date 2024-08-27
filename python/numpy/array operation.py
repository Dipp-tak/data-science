#Basics operation with Arrays.

#Import Numpy
import numpy as np

#Create two Arrays and print than.
arr = np.array([1,2,3])
ones_arr = np.ones(3)
print("This is 1st Array:",arr)
print("This is 2nd Array:",ones_arr)

#Add two Arrays.
add_arr = arr + ones_arr
print("Sum of 1st And 2nd Array: ",add_arr)

#Subtract two Arrays.
sub_arr = arr - ones_arr
print("Substracting 1st Array from 2nd Array: ",sub_arr)

#Create An another Array and print it.
arr2 = np.array([4,5,6])
print("This is 3rd Array:",arr2)

#multiply two Arrays
mul_arr = arr * arr2
print("Multiplication of 1st and 3rd Array:",mul_arr)

#Multiply 5 with each element.
mul_5 = arr * 5
print("Multiply 1st Array with value 5: ",mul_5)

#Division of two Arrays.
div_arr = arr / arr
print("1st Array divided by 1st Array",div_arr)

#Sum of all element in Array.
sum_value = arr.sum()
print("Sum of All values in A Array(1st-Array): ",sum_value)

#Mean of all element in Array.
mean_value = arr.mean()
print("Mean of All values in A Array(1st-Array): ",mean_value)

#Product of all element in Array.
product_value = arr.prod()
print("Product of All values in A Array(1st-Array): ",product_value)

#Maimum valu of a array
max_value = arr.max()
print("Maximum value of a Array(1st-Array): ",max_value)

#Minimum valu of a array
min_value = arr.min()
print("Minimum value of a Array(1st-Array): ",min_value)

#Create a 2-D Array and print it
arr_2d = np.array([[4,5],[6,7]])
print("This is a 2-D Array: \n",arr_2d)

#Sum over the axis of rows
row_arr = arr_2d.sum(axis = 0)
print("Sum over the row axis(2-D Array)",row_arr)

#Sum over the axis of columns with
colm_arr = arr_2d.sum(axis = 1)
print("Sum over the column axis(2-D Array)",colm_arr)
