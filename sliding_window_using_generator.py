# Problem:
# Create a generator function called sliding_window(sequence, size) that yields all possible contiguous sub‑sequences (windows) of length size from the given sequence.
# Requirements:
# - The generator should not build all windows in memory at once—it should yield them one by one.
# - If the size is larger than the sequence length, the generator should yield nothing.
# - Example:
# list(sliding_window([1, 2, 3, 4, 5], 3))


# - should produce:
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

class Sliding_window:
    def __init__(self, sequence, size):
        self.sequence = sequence
        self.size = size

    def generator(self):
        s = 0
        e = s + self.size
        while e <= len(self.sequence):
            yield self.sequence[s:e]
            s += 1
            e += 1

s = Sliding_window([1, 2, 3, 4, 5], 3)
# l = []
# print(s.generator())

# for i in s.generator():
#     l.append(i)

# print(l)
print(list(s.generator()))