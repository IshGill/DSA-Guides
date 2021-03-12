prompt = int(input("Enter number of rows: "))
for rows in range(prompt):
    for columns in range (prompt):
        if columns == prompt-1 or rows== (prompt-1) or columns == (prompt-rows-1):
            print('*', end='')
        else:
            print(end=' ')
    print()