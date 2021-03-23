def get_gcd(num1, num2):
    while num1 % num2 != 0:
        old_num1 = num1
        old_num2 = num2
        num1 = old_num2
        num2 = old_num1
    return num2

print(get_gcd(10,100))