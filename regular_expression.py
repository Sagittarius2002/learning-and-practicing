import re

text = "My number is 9876543210"
m = re.search(r"\d{10}", text)
print(m.group())   # 9876543210

text = "Hello Sayan"
print(re.match(r"Hello", text))   # ✅ Match
print(re.match(r"Sayan", text))   # ❌ None

text = "Hello Sayan"
m = re.search(r"Sayan", text)
print(m.group())   # Sayan

text = "Sayan Hello"
print(re.match(r"Sayan", text).group())   # Sayan

text = "Emails: a@x.com, b@y.org, c@z.net"
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
print(emails)  
# ['a@x.com', 'b@y.org', 'c@z.net']

text = "My number is 9876543210"
masked = re.sub(r"\d", "*", text)
print(masked)  
# My number is **********

text = "My number is 9876543210"

masked = re.sub(r"(\d{6})(\d{4})", r"******\2", text)
print(masked)

masked = re.sub(r"(\d{2})\d{6}(\d{2})", r"\1******\2", text)
print(masked)

masked = re.sub(r"(\d{2})\d+(\d{2})", r"\1******\2", text)
print(masked)

# When you use re.match() or re.search(), Python returns a Match object if the pattern is found.
# That object contains details about the match (start, end, span, groups, etc.).
# - .group() → returns the actual substring that was matched.
# - By default, .group() is the same as .group(0) → the whole match.
# - If you use capturing groups in your regex (with parentheses ()), you can access them with .group(1), .group(2), etc.

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))        # 6
print(add_numbers(5, 10, 15, 20))  # 50

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Sayan", role="Data Engineer", city="Kolkata")
# name: Sayan
# role: Data Engineer
# city: Kolkata

# “Default arguments let you assign fallback values to parameters, so they become optional. 
# Variable‑length arguments (*args, **kwargs) let you accept an arbitrary number of positional or keyword arguments. 
# Together, they make functions flexible and reusable.”
