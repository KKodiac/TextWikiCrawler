import pandas as pd

data = pd.read_csv("DataFile/data.csv, sep='\t', names=['word', 'tense', 'link'], header=None)

data.head()
