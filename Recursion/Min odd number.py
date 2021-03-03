def get_min_odd(numbers):
    if len(numbers) == 1:
        if numbers[0] % 2 == 0:
            return 9999
        else:
            return numbers[0]

    if numbers[0] < numbers[1] and numbers[0] % 2 != 0:
        numbers.append(numbers[0])
        return(get_min_odd(numbers[1:]))
    else:
        return(get_min_odd(numbers[1:])) 
    



lst = [6, 4, 5, 9]
print(get_min_odd(lst))
print(get_min_odd([2]))
