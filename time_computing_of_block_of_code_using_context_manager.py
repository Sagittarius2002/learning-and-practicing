# Problem:
# Design a custom context manager called Timer that measures how long a block of code takes to execute.
# Requirements:
# - When entering the context (__enter__), it should record the start time.
# - When exiting (__exit__), it should record the end time and print the total elapsed time in seconds.
# - It should work even if an exception occurs inside the with block (i.e., still print the elapsed time).
# - Bonus: Allow the user to optionally pass a label (like "DB Query" or "Sorting") so the output is more descriptive.

# Example

# class MyContext:
#     def __enter__(self):
#         print("Entering context...")
#         return "Resource Ready"
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context...")
#         if exc_type:
#             print(f"An exception occurred: {exc_value}")
#         return True  # suppress exception if needed

# # Usage
# with MyContext() as resource:
#     print(resource)

import time

class TimeCalculation:

    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exec_type, exec_value, traceback):
        end = time.time()
        elapsed = end - self.start
        print(f"{self.label} Elapsed Time: {elapsed}")
        

s = "Loop Execution"
with TimeCalculation(s) as t:
    c = 0
    for i in range(20000):
        c += 1


#  In case there is exception
#  class Suppressor:
#     def __enter__(self):
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print(f"Suppressed: {exc_type.__name__}")
#             return True   # suppress the exception

# with Suppressor():
#     print("Before error")
#     1 / 0
#     print("After error")  # This line still runs!

# Before error
# Suppressed: ZeroDivisionError
# After error

# - You use them to log, clean up, or suppress exceptions.

# import traceback

# class DebugContext:
#     def __enter__(self):
#         print("Entering context...")
#         return self
    
#     def __exit__(self, exc_type, exc_value, tb):
#         if exc_type:
#             print(f"Exception type   : {exc_type.__name__}")
#             print(f"Exception value  : {exc_value}")
#             print("Traceback details:")
#             traceback.print_tb(tb)   # pretty-print the traceback
#         print("Exiting context...")
#         # return False so the exception propagates after logging
#         return False

# # Usage
# with DebugContext():
#     print("Inside block")
#     1 / 0   # deliberate ZeroDivisionError

# Entering context...
# Inside block
# Exception type   : ZeroDivisionError
# Exception value  : division by zero
# Traceback details:
#   File "example.py", line 18, in <module>
#     1 / 0
# Exiting context...
# Traceback (most recent call last):
#   ...
# ZeroDivisionError: division by zero