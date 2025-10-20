student = {
    "name": "Sayan",
    "age": 25,
    "skills": ["Python", "SQL", "NumPy"]
}

print(student["name"])       # Sayan
print(student.get("age"))    # 25
print(student.get("grade", "N/A"))  # Safe access with default

student["city"] = "Kolkata"   # add new key
student["age"] = 26           # update existing key

student.pop("city")           # remove by key
student.popitem()             # remove last inserted item
del student["age"]            # delete by key
student.clear()               # remove all items

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, ":", value)

extra = {"grade": "A"}
student.update(extra)

company = {
    "emp1": {"name": "Alice", "dept": "IT"},
    "emp2": {"name": "Bob", "dept": "HR"}
}
print(company["emp1"]["name"])  # Alice

# - Dictionaries = hash maps in Python.
# - Keys must be unique & immutable.
# - Values can be anything.
# - Extremely versatile: configs, JSON, lookups, caching
