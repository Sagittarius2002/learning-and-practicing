# - CSV = Comma Separated Values.
# - A plain text format where each line is a row, and values are separated by commas (or sometimes tabs/semicolons).

import csv

with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv

data = [
    ["name", "age", "city"],
    ["Sayan", 25, "Kolkata"],
    ["Alice", 30, "Delhi"]
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

import csv

with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["city"]) # treat each row as columns

import pandas as pd

df = pd.read_csv("people.csv")
print(df)

# Write back
df.to_csv("output.csv", index=False)

# “CSV handling in Python can be done with the built‑in csv module for lightweight operations, 
# or with Pandas for data analysis. csv.reader/writer work with lists, while DictReader/DictWriter map rows to dictionaries 
# for easier column access.”
