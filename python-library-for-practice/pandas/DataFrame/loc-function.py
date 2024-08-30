#Selecting a row
#import pandas for use
import pandas as pd

#Create A DataFrame
my_df = pd.DataFrame({
    'Name':['Doraemon','Shinchan','Hattori','Kiteretsu'],
    'Email':['doraemon.catrobot@gmail.com','shinchan.naughty@gmail.com','hattori.ninja@gmail.com','kiteretsu.scientist@gmail.com']
})

#Use the loc function to selet a row
my_df.loc[2]
