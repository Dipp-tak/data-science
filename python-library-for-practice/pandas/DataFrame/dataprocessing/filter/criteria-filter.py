#Filter Multipule values
#Import pandas for use
import pandas as pd

#Import Dataset
url  = 'https://raw.githubusercontent.com/Dipp-tak/data-science/main/python-library-for-practice/pandas/dataset_large.csv'
df = pd.read_csv(url)
#print those who scored above 85
high_score = (df['Score']>85)
df.loc[high_score]
