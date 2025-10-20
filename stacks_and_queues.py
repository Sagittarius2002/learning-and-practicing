stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)  # [10, 20, 30]

# Pop
print(stack.pop())  # 30
print(stack)        # [10, 20]

from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)  # deque([10, 20, 30])

# Dequeue
print(queue.popleft())  # 10
print(queue)            # deque([20, 30])

# - Stack → can also be implemented with collections.deque (faster than list for pops).
# - Queue → deque is the go‑to, but Python also has queue.Queue for thread‑safe operations.
# - Priority Queue → implemented with heapq (min‑heap).

# - Stack → LIFO, use .append() and .pop().
# - Queue → FIFO, use deque.append() and deque.popleft().
# - Both are abstract data types with real‑world analogies.
# - Foundation for algorithms like DFS (stack) and BFS (queue).

queue.pop()
print(queue)