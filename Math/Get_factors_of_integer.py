number = int(input("Enter number to factor: "))
factors = [n for n in range(1, number + 1) if number % n == 0]
print(factors)