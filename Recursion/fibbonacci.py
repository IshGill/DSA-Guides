# Basic fibbonacci sequence recursive function
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(6))

# Fibbonacci sequence with memoization
def fibM(n, memo={}):
    if n in memo:
        return memo[n]
    elif n < 2:
        return n
    else:
        memo[n] = fibM(n-1) + fibM(n-2)
        return fibM(n-1) + fibM(n-2)

print(fibM(7))
