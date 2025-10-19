import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Delta', 'Blue', 'Sayan'],
    'Age': [10, 12, 68, 21, 21, 23],
    'City': ['Mumbai', 'Delhi', 'Kolkata', 'Delhi', 'Bangalore', 'Kolkata']
}

df = pd.DataFrame(data)
print(df)

import numpy as np

arr = np.arange(9).reshape(3, 3)
df2 = pd.DataFrame(arr, columns = ['A', 'B', 'C'])
print(df2)

print(df['Name'])

print(df.loc[0])
print(df.loc[0:2, 'City'])
print(df.iloc[1])
print(df.iloc[0:2, 1:3])

print(df[df['Age'] > 20])
df['Salary'] = [10000, 20000, 30000, 40000, 50000, 60000]
print(df)
print(df.drop('Age', axis = 1))
print(df.drop(2, axis = 0))

print(df.sort_values(by = 'Salary', ascending = False))
# print(df)

print(df[df['City'] == 'Kolkata'])
print(df[(df['Age'] == 23) & (df['City'] == 'Kolkata')])