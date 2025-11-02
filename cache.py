from functools import cache

@cache
def fib(n):
    return fib(n-1) + fib(n-2) if n > 1 else n

for i in range(100):
    print(fib(i))