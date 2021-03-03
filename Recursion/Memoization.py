import time
def fibonacci(i, cache={}):
    if i in cache:
        return cache[i]
    if i < 2:
        return i
    else:
        cache[i] = fibonacci(i-1) + fibonacci(i-2)
        return fibonacci(i-1) + fibonacci(i-2)

start = time.time()

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))
print(fibonacci(8))
# print(fibonacci(9))
# print(fibonacci(12))
# print(fibonacci(32))
# print(fibonacci(52))
end = time.time()
print(end - start)


