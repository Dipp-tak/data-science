#Changing the index of DataFrame
#import pandas for use
import pandas as pd

#Create A DataFrame
my_df = pd.DataFrame({
    'Name':['Doraemon','Shinchan','Hattori','Kiteretsu'],
    'Email':['doraemon.catrobot@gmail.com','shinchan.naughty@gmail.com','hattori.ninja@gmail.com','kiteretsu.scientist@gmail.com]']
})

my_df = my_df.set_index(pd.Index(['Robot','Boy','Ninja','Scientist']))
my_df
