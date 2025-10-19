# Create a custom iterator class called EvenNumbers that takes a start and end value. The iterator should return only the even numbers in that range, one at a time, and stop when the range is exhausted.
# Requirements:
# - Implement __iter__() and __next__() methods.
# - If the range has no even numbers, the iterator should stop immediately.
# - Demonstrate its use in a for loop.

class EvenNumbers:
    def __init__(self, start, stop):
        self.current = start
        self.limit = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.current <= self.limit:
            val = self.current
            if val % 2 == 0:
                self.current += 1
                return val
            self.current += 1
        else:
            raise StopIteration
    
for i in EvenNumbers(10, 18):
    print(i)