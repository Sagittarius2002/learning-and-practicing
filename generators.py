# - A generator is a special type of function that produces values one at a time instead of returning them all at once.
# - It uses the yield keyword instead of return.
# - Generators are lazy: they generate values only when requested, saving memory.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause here, return value
        i += 1

gen = count_up_to(5)
print(next(gen))  # 1
print(next(gen))  # 2
print(list(gen))  # [3, 4, 5]

# Generator Expressions
# Like list comprehensions, but with parentheses → memory‑efficient.
squares = (x**2 for x in range(5))
print(next(squares))  # 0
print(list(squares))  # [1, 4, 9, 16]

# - Memory efficiency: don’t store the whole sequence in memory.
# - Performance: compute values on demand.
# - Streaming data: perfect for reading large files, logs, or infinite sequences

def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()