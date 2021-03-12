# #Right angle triangle
# rows = int(input("Rows: "))
# columns = int(input("Columns: "))
# for i in range(rows-1,-1,-1):
#     print(i * " " + (columns-i) * "*")
#
# #Flipped right angle triangle
# rows = int(input("Rows: "))
# columns = int(input("Columns: "))
# for i in range(rows):
#     print(i * " " + (columns - i) * "*")
#
# #Parallelogram
# rows = 5
# columns = 5
# for i in range(rows-1,-1,-1):
#     print(i*" "+rows*"*")

# #Flipped opposite right angle triangle
# rows = 5
# columns = 5
# for i in range(rows):
#     print((columns-i) * "e" + i * " ")

# for i in range(1,6):
#     for j in range(6-i):
#         print("e", end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()

# rows = 6
# for i in range(1, rows):
#     print((rows-i) * " " + i * "* " + i * " ")

# Filled even triangle
# size = 10
# count = 0
# for i in range(2, size+2, 2):
#     count += 1
#     curry = size//2 + count
#     print((curry - i)* " ",end="")
#     if i < size:
#         print("X" + (i-2) * "-" + "X")
#     else:
#         print(i * "X")
#
# #Filled odd triangle
# size = 5
# count = 0
# for i in range(1, size + 1, 2):
#     count += 1
#     curry = size//2 + count
#     print((curry - i)* " ",end="")
#     if i < size and i > (size//2):
#         print("X" + (i-2) * "-" + "X")
#     else:
#         print(i * "X")

#Filled even or odd triangle function
# def draw_triangle(size=5):
#     try:
#         # size = int(input("Enter a size: "))
#         if size <= 2:
#             raise ValueError()
#         else:
#             count = 0
#             if size % 2 == 0:
#                 for i in range(2, size + 2, 2):
#                     count += 1
#                     curry = size // 2 + count
#                     print((curry - i) * " ", end="")
#                     if i < size:
#                         print("X" + (i - 2) * "-" + "X")
#                     else:
#                         print(i * "X")
#             else:
#                 for i in range(1, size + 1, 2):
#                     count += 1
#                     curry = size//2 + count
#                     print((curry - i)* " ",end="")
#                     if i < size and i > (size//2):
#                         print("X" + (i-2) * "-" + "X")
#                     else:
#                         print(i * "X")
#     except TypeError:
#         print("ERROR: Invalid input!")
#     except ValueError:
#         print("ERROR: The size is too small.")
#
# if __name__ == '__main__':
#     draw_triangle()
#     draw_triangle(2)
#     draw_triangle(10)
#     draw_triangle("two")

#Hollow right angle triangle 
# prompt = int(input("Enter number of rows: "))
# for rows in range(prompt):
#     for columns in range (prompt):
#         if columns == prompt-1 or rows== (prompt-1) or columns == (prompt-rows-1):
#             print('*', end='')
#         else:
#             print(end=' ')
#     print()