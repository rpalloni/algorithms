# Fibonacci sequence: 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
# nth number is the sum of the previous two, e.g: 2+3=5, 3+5=8 ...

import time

# find the nth Fibonacci number
def fibonacci_n(n):
    if n in {0, 1}:
        return n
    else:
        return fibonacci_n(n-1) + fibonacci_n(n-2)

start = time.time()
fibonacci_n(10) # 55
end = time.time()
print(f'{end - start:.20f} seconds')


# find the Fibonacci sequence up to the nth number
# iterative
def fibonacci_iter(n):
    # 1st sequence number
    if n == 1:
        return [0]
    # initialize seq
    arr = [0, 1]
    for i in range(2, n):
        arr.append(arr[-1]+arr[-2])
    return arr

start = time.time()
fibonacci_iter(25) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
end = time.time()
print(f'{end - start:.20f} seconds')


# recursive
def fibonacci_recu(n):
    print(n)
    if n < 2:
        return [0]
    if n < 3:
        return [0, 1]
    arr = fibonacci_recu(n-1)
    arr.append(arr[n-2] + arr[n-3])

    return arr

start = time.time()
fibonacci_recu(25)
end = time.time()
print(f'{end - start:.20f} seconds')


# generator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

def fibonacci_gen(n):
    g = fibonacci_generator()
    return [next(g) for _ in range(n)]

start = time.time()
fibonacci_gen(25)
end = time.time()
print(f'{end - start:.20f} seconds')
