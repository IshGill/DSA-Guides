def get_gcd(num1, num2):
    #If the two  numbers are incorrect order ie, num1 should
    #always be larger for our mod operation, hence if in
    #incorrect order call the function and swap both parameters
    if num2 > num1:
        get_gcd(num2, num1)
    #If equivalnce class = 0 this implies multiples hence
    #clean divisor 
    elif num1 % num2 == 0:
        return num2
    #If not congruent to 0 then make num2 = first parameter
    #make the mod output of num1 % num2 = num2 parameter
    return get_gcd(num2, num1 % num2)

print(get_gcd(100, 70))
print(get_gcd(2, 6))
