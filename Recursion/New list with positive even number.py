def get_positive_even_list(numbers,var=[]):
    if len(numbers) == 0:
        return var
    if numbers[0] % 2 == 0 and numbers[0] > 0:
        numbers.append(numbers[0])
        return get_positive_even_list(numbers[1:])
    else:
        return get_positive_even_list(numbers[1:])

print("{}".format(get_positive_even_list([2, 3, -5, -6, 8, 5, 9, 10])))
print("{}".format(get_positive_even_list([-1, 0, 1])))
