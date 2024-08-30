#Import Pandas 
import pandas as pd

#Create A data Frame
my_df = pd.DataFrame({'Numbers':[10,20,30,40,50],'Numbers_2':[67,79,88,93,10]})

#Check some logical condition

#Numbers Greter than 35 
my_df['Logic'] = my_df["Numbers"]>35

#Numbers Less than 80
my_df['Logic_2'] = my_df["Numbers_2"]<80

# Print the new Data Frame
my_df
