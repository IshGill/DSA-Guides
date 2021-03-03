def factorial_loop(n):
    fact_count = 1
    for i in range(n, 0, -1):
        fact_count *= i
    return fact_count

print(factorial_loop(0))

def recursive_fact(n):
    if n <= 0:
        return 1
    else:
        return n*recursive_fact(n-1)

print(recursive_fact(7))