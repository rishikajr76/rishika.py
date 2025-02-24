# Reading a CSV file and checking for missing values
import pandas as pd
df = pd.read_csv('data.csv')  
df.head()  
print(df.isnull().sum())