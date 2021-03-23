def checkPrime(n):
    return "{} is not prime".format(n) if len([i for i in range(2, n) if n % i == 0]) >= 1 else "{} is prime".format(n)

print(checkPrime(7))