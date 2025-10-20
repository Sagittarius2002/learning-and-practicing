# {key_expr: value_expr for item in iterable if condition}

nums = [1, 2, 3, 4]
squares = {x: x**2 for x in nums}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16}

even_squares = {x: x**2 for x in nums if x % 2 == 0}
print(even_squares)  # {2: 4, 4: 16}

prices = {'apple': 100, 'banana': 40, 'cherry': 60}
discounted = {fruit: price*0.9 for fruit, price in prices.items()}
print(discounted)  # {'apple': 90.0, 'banana': 36.0, 'cherry': 54.0}

# {expression for item in iterable if condition}

nums = [1, 2, 2, 3, 3, 4]
unique_squares = {x**2 for x in nums}
print(unique_squares)  # {16, 1, 4, 9}

evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}

pairs = {(x, y) for x in [1, 2] for y in ['a', 'b']}
print(pairs)  # {(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')}

# - Dict comprehensions → build dictionaries quickly, often from lists or existing dicts.
# - Set comprehensions → build sets with uniqueness guaranteed.
# - Both support conditions and nested loops.
# - Cleaner and faster than writing explicit loops.
