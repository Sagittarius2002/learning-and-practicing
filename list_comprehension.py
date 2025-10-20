# [expression for item in iterable if condition]
# - expression → what to compute/return
# - item → variable representing each element
# - iterable → sequence (list, range, etc.)
# - condition (optional) → filter element

nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares)  # [1, 4, 9, 16, 25]

evens = [x for x in nums if x % 2 == 0]
print(evens)  # [2, 4]

pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs)
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

def square(x): return x**2
squares = [square(x) for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]

nums = [1, 2, 3]
squares_dict = {x: x**2 for x in nums}
print(squares_dict)  # {1: 1, 2: 4, 3: 9}

nums = [1, 2, 2, 3, 3]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # {1, 4, 9}