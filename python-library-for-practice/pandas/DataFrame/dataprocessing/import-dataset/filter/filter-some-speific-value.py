#Data filtering with pandas
#Import pandas as pd
import pandas as pd

#Import Dataset from github
url ='https://raw.githubusercontent.com/Dipp-tak/data-science/main/python-library-for-practice/pandas/DataFrame/dataprocessing/import-dataset/practice-dataset.csv'
df = pd.read_csv(url)

#Select those student who comes from 'USA'
filt = (df['Country'] == 'USA')
df[filt]
