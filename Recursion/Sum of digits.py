def get_sum_digits(number):
    if number < 10:
        return number
    else:
        return (number % 10) + get_sum_digits(number//10)
print(234, ":", get_sum_digits(234))
print(106, ":", get_sum_digits(106))
