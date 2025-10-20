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

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 40],
    'City': ['Kolkata', 'Delhi', None, 'Mumbai']
}
df = pd.DataFrame(data)

print(df.isna())       # Boolean mask of missing values
print(df.isna().sum()) # Count missing values per column

# Fill with a constant
# df['Age'] = df['Age'].fillna(0)

# Fill with column mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Forward fill (propagate previous value)
# df['City'] = df['City'].fillna(method='ffill')

# Backward fill (propagate next value)
df['City'] = df['City'].fillna(method='bfill')

print(df)

# Drop rows with any NaN
df_drop_rows = df.dropna()

# Drop columns with any NaN
df_drop_cols = df.dropna(axis=1)

# Drop rows only if *all* values are NaN
df_drop_all = df.dropna(how='all')

# Drop rows if specific column(s) have NaN
df_drop_subset = df.dropna(subset=['Age'])

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Age': [25, 30, 35, 25, 30],
    'City': ['Kolkata', 'Delhi', 'Mumbai', 'Kolkata', 'Delhi']
}
df = pd.DataFrame(data)

print(df.duplicated())       # Boolean mask: True if row is duplicate
print(df.duplicated().sum()) # Count duplicates

df_unique = df.drop_duplicates()

df.drop_duplicates(keep='first')

df.drop_duplicates(keep='last')

df.drop_duplicates(keep=False)

df.drop_duplicates(subset=['Name']) # only looking towards specific columns

df.drop_duplicates(inplace=True) #modify the dataframe directly

print(df)

import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Rename specific columns
df = df.rename(columns={'A': 'Age', 'B': 'Salary'})
print(df)

df = df.rename(index={0: 'row1', 1: 'row2', 2: 'row3'})
print(df)

df.columns = ['Employee_Age', 'Employee_Salary']
print(df)

df.index = ['emp1', 'emp2', 'emp3']
print(df)

df.rename(columns={'Employee_Age': 'Age'}, inplace=True)

import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Salary': [60000, 50000, 65000, 70000, 52000, 72000],
    'Experience': [2, 5, 3, 10, 4, 12]
}
df = pd.DataFrame(data)

print(df)

print(df.groupby('Department')['Salary'].mean())

print(df.groupby('Department')['Salary'].agg(['mean', 'max', 'min']))

print(df.groupby('Department').agg({
    'Salary': 'mean',
    'Experience': 'max'
}))

print(df.groupby(['Department', 'Experience'])['Salary'].mean())

print(df.groupby('Department')['Salary'].mean().reset_index())

import pandas as pd

data = {
    'Department': ['IT', 'IT', 'HR', 'HR'],
    'Employee': ['A', 'B', 'C', 'D'],
    'Salary': [60000, 65000, 50000, 52000],
    'Year': [2023, 2024, 2023, 2024]
}
df = pd.DataFrame(data)

# Pivot: rows = Department, columns = Year, values = Salary
pivoted = df.pivot(index='Department', columns='Year', values='Salary')
print(pivoted)

# Pivot table with aggregation
pivot_tbl = pd.pivot_table(
    df,
    index='Department',
    columns='Year',
    values='Salary',
    aggfunc='mean'   # could be sum, max, min, etc.
)
print(pivot_tbl)

pivot_multi = pd.pivot_table(
    df,
    index='Department',
    values='Salary',
    aggfunc=['mean', 'max', 'min']
)
print(pivot_multi)

import pandas as pd

# - Works only on a Series (1D).
# - Applies a function, dict, or lambda to each element.

s = pd.Series([1, 2, 3, 4])

print(s.map(lambda x: x**2))   # square each element
print(s.map({1: 'one', 2: 'two'}))  # map values via dict

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

# - On a Series → behaves like map.
# - On a DataFrame → applies function along an axis.

# Apply to Series
print(df['A'].apply(lambda x: x**2))

# Apply to DataFrame (column‑wise)
print(df.apply(sum, axis=0))   # sum of each column

# Apply to DataFrame (row‑wise)
print(df.apply(sum, axis=1))   # sum of each row

# - Works only on DataFrames.
# - Applies a function to every element.

print(df.applymap(lambda x: x * 2))

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 62, 90]
})

# Apply lambda to a column
df['Grade'] = df['Marks'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')

# Use lambda with multiple columns
df['Name_Length'] = df.apply(lambda row: len(row['Name']), axis=1)

print(df)

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Marks': [85, 62, 90]
})

# Apply lambda to a column
df['Grade'] = df['Marks'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')

# Use lambda with multiple columns
df['Name_Length'] = df.apply(lambda row: len(row['Name']), axis=1)

print(df)

s = pd.Series([10, 20, 30])

# Convert to percentage string
percent = s.apply(lambda x: str(x) + '%')
print(percent)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

# Row‑wise sum using lambda
row_sum = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(row_sum)

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

# Multiply every element by 2
doubled = df.applymap(lambda x: x * 2)
print(doubled)

nums = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16, 25]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

from functools import reduce

# Compute product of all numbers
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120

nums = [1, 2, 3, 4, 5]

# Square each number
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16, 25]

# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

from functools import reduce

# Compute product of all numbers
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120

nums = [1, 2, 3, 4, 5, 6]

# Step 1: Square each number (map)
squares = list(map(lambda x: x**2, nums))

# Step 2: Keep only numbers > 10 (filter)
filtered = list(filter(lambda x: x > 10, squares))

# Step 3: Sum them up (reduce)
total = reduce(lambda x, y: x + y, filtered)

print("Squares:", squares)     # [1, 4, 9, 16, 25, 36]
print("Filtered:", filtered)   # [16, 25, 36]
print("Total:", total)         # 77

