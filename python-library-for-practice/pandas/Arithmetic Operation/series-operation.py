#See the Arithmetic Operation in Pandas
#Import Numpy For macking Arrays
import numpy as np
#Import Pandas 
import pandas as pd

#By using numpy create two Arrays
my_arr = np.ones(5)
my_arr1 = np.arange(5)

#From Arrays Create Series
my_Series = pd.Series(my_arr)
my_Series1 = pd.Series(my_arr1)
print("1st Series is : \n",my_Series,'\n')
print("2nd Series is : \n",my_Series1,"\n")

Add_Series = my_Series + my_Series1
print("1st Series + 2nd Series \n",Add_Series,'\n')

Sub_Series = my_Series1 - my_Series
print("2nd Series - 1st Series \n",Sub_Series,'n')

Mul_Series = my_Series * my_Series1
print("1st Series * 2nd Series \n",Mul_Series,'n')

Div_Series = my_Series / my_Series1
print("1st Series + 2nd Series \n",Div_Series)
