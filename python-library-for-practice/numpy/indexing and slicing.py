#Import numpy.
import numpy as np

#Create a Array and print it.
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("The Array is : ",arr)

#Access the element of array using index.
#Array's Name[Index].
#In Array indexing start with 0.
print("Print the 1st element of Array : ",arr[0]) 

#Print Index the 8.
print("Print the elemnet whose index is 8: ",arr[8])

#Print with using negative index.
print("Print the element whose index is -5: ",arr[-5])

#Slicing the Array

#Print Element less than 10.
less_10 = arr[arr<10]
print("Print elements less than 10",less_10)

#Print Element greater than 10.
greater_10 = (arr>10)
print("print elements greater than 10",arr[greater_10])

#let's print greater than 5 and less than 11.
bwt = ((arr>5) & (arr<11))
print("print the elements greater than 5 and below than10:",arr[bwt])

#Let's Print element divisible by 3.
div = (arr % 3 == 0)
print("Print the elements divided by 3 :",arr[div])

#Let's Print element with index slicingsling.
slic_data = arr[0:5]
print("The elements upto index 4 is:",slic_data)

#Print the element between index 5 to 11.
slic_data2 = arr[5:11]
print("The elements between index 5 and 11:",slic_data2)

#Print the element 5,6,7,8 and 9 with using negative index.
neg_slic_data = arr[-11:-6]
print("Print 5,6,7,8 and 9 with uing negative index",neg_slic_data)
