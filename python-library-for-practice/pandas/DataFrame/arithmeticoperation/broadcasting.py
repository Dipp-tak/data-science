#Import Pandas 
import pandas as pd

#Create A data Frame
my_df = pd.DataFrame({'Numbers':[1,2,3,4,5],'Numbers_2':[6,7,8,9,10]})

#multiply column-1 with 5 and save it
my_df['Numbers'] = my_df['Numbers'] * 5

# Print the new Data Frame
my_df
