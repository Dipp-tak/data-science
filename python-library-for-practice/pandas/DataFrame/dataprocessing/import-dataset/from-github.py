#Use dataset from github
#Import Pandas for use
import pandas as pd

#Import the dataset from github by copying the raw url
url = 'https://raw.githubusercontent.com/Dipp-tak/data-science/main/python-library-for-practice/pandas/DataFrame/dataprocessing/import-dataset/practice-dataset.csv'
df = pd.read_csv(url)
df
