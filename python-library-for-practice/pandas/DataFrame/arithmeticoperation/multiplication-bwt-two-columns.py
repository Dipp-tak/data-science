#Import Pandas 
import pandas as pd

#Create A data Frame
my_df = pd.DataFrame({'Numbers':[1,2,3,4,5],'Numbers_2':[6,7,8,9,10]})

#Multiplication operation between two columns
my_df['Result_Numbers'] = my_df['Numbers'] * my_df['Numbers_2']

# Print the Data Frame where we have the multiplication value in another column[Result_Numbers]
my_df
