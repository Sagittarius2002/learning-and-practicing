import time

def fibonacci_using_recursion(a, b, n):
    if ((a + b) > n):
        return
    else:
        s = a + b
        a = b
        b = s
        print(s)
        return fibonacci_using_recursion(a, b, n)

def fibonacci(limit):
    a = 0
    b = 1
    def addition():
        nonlocal limit
        nonlocal a
        nonlocal b
        sum = a + b
        if sum <= limit:
            a = b
            b = sum
            print(sum)
            return a, b

    return addition

n = int(input('Enter fibonacci limit: '))
f = fibonacci(n)
a = 0
b = 1
print('Fibonacci using closures--------- ')
x = time.time()
print(a)
print(b)
while(1):
    if(f()):
        f()
    else:
        break
y = time.time()

print('Elapsed Time: ', y - x)

a = 0
b = 1
print('Fibonacci using loops---------- ')
x = time.perf_counter()
print(a)
print(b)   
while((a + b) <= n):
    s = a + b
    print(s)
    a = b
    b = s
y = time.perf_counter()

print('Elapsed Time: ', y - x)

a = 0
b = 1
print('Fibonacci using recursion---------- ')
x = time.time()
print(a)
print(b)
fibonacci_using_recursion(a, b, n)
y = time.time()
print('Elapsed Time: ', y - x)