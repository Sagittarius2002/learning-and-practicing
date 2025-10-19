# Problem:
# Build a closure called make_counter that returns two functions:
# - increment() → increases the counter by 1 and returns the new value.
# - decrement() → decreases the counter by 1 and returns the new value.
# Requirements:
# - The counter should “remember” its state across calls, even after the outer function has finished.
# - Each call to make_counter() should create an independent counter.
# - Bonus: Allow the counter to start from a custom initial value.

def make_counter(num):
    def i_or_d(s):
        nonlocal num
        if s == "increment":
            num += 1
            return num
        if s == "decrement":
            num -= 1
            return num
    return i_or_d
    
counter1 = make_counter(10)

print(counter1("increment"))  # 11
print(counter1("increment"))  # 12
print(counter1("decrement"))  # 11

counter2 = make_counter(0)

print(counter2("increment"))  # 1
print(counter2("decrement"))  # 0
