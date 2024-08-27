#Where we see The series Data Structure and some operation on it.
#Import pandas for use in codes.
import pandas as pd

#Create a list and print it.
my_list = [1,2,3,4,5]
print("The list is : ",my_list)

#Create a series from the list and print it.
my_series = pd.Series(my_list)
print("The series is :\n",my_series)

#Check the type of series
print(type(my_series))

#Prin Series element with index
print("index 0 element is:",my_series[0])
print("index 4 element is:",my_series[4])

#Change the index of series
my_series = pd.Series(my_list,index=['a','b','c','d','e'])
print("Change the index to a,b,c,d and e: \n",my_series)

#Change the data type of Series
my_series = pd.Series(my_list,dtype=float)
print("The series is :\n",my_series)

#Create a series from dictionary
my_dict = {'a':'Apple','b':'Ball','c':'Cat','d':'Dog','e':'Egg'}
my_series = pd.Series(my_dict)
print("The series is :\n",my_series)
