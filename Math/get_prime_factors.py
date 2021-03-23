def getPrimeFactors(n):
    i = 2
    prime_factors = []
    while i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n /= i
        else:
            i += 1
    return prime_factors

print(getPrimeFactors(5))