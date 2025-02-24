# Creating a DataFrame
import pandas as pd
data = {'Name': ['Ria', 'Mia', 'Jack'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)
print(df)