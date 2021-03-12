number = int(input("Enter number of rows: "))
if number == 3:
    print("*" * 3)
    print("*" * 3)
    print("*" * 3)
else:
    print("*" * number)
    print("*" * 2, " " * (number-4), "*" * 2, sep= "")
    count1 = 1
    for i in range(2, int((number - 1)/2)):
        count2 = (number - 4) - (2 * count1)
        print("*", " " * count1, "*", " " * count2, "*", " " * count1, "*", sep= "")
        count1 += 1
    print("*", " " * int((number-3)/2), "*", " " * int((number-3)/2), "*", sep= "")
    count2 = 1
    for row in range(int((number-1)/2)+1, number-2):
        count1 = int((number-(4 + count2))/2)
        print("*", " " * count1, "*", " " * count2, "*", " " * count1, "*", sep= "")
        count2 += 2
    print("*" * 2, " " * int(number-4), "" * int(number), "*" * 2, sep= "")
    print("*" * number)
