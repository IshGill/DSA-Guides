#We want to print the values in the upper and lower quartile of our list
#The lower quartile is the value which is 25% larger than all other values in the list
#The upper quartile value is the value for which 75% of the list elements are smaller than
#This is a simple process all we require is to give the value which is at the 25% and 75% indexes
#of the list.
def get_quartiles(list_of_numbers):
    list_of_numbers.sort()
    #We must sort the list!
    lower_quartile = int(len(list_of_numbers) * 0.25)
    #Simply take the lenth of the list and mutliply it by 0.25
    #The length of the list in a percentage is 100% and we want 25% from this 100%
    #Therefore when we multiply the length of the list by 0.25 we derive the value which
    #is equivalent to 25% of the length of the list
    upper_quartile = int(len(list_of_numbers) * 0.75)
    #We want the 75% index value of the list. Therefore we mutiply by 0.75 which gives us
    #the 75% index out of the 100% index of the list
    median_quartile = int(len(list_of_numbers) * 0.5)
    #This will give us the index right in the middle of the list
    return list_of_numbers[lower_quartile], list_of_numbers[upper_quartile]

if __name__ == '__main__':
    print(get_quartiles([12, 5, 22, 30, 7, 36, 14, 42, 15, 53, 25]))
    print(get_quartiles([5, 1, 4, 2, 3]))
    print(get_quartiles([10, 40, 30, 99]))
    print(get_quartiles([10]))
    print(get_quartiles([12, 5, 22, 30, 7, 36, 14, 42, 15, 53, 25, 65]))


def get_middle_number(numbers):
    numbers.sort()
    return numbers[int(len(numbers) * .5)]

if __name__ == '__main__':
    numbers3 = [18, 9, 8, 5, 12, 25, 4, 3, 7]  #if sorted [3, 4, 5, 7, 8, 9, 12, 18, 25]
    numbers4 = [8, 24, 4, 10, 10, 25, 23, 21, 24, 5, 4, 6, 23, 23, 19]
    print("3.", get_middle_number(numbers3))
    print("4.", get_middle_number(numbers4))
    numbers1 = [20, 24, 3, 8, 9]  # if sorted [3, 8, 9, 20, 24]
    numbers2 = [15, 28, 22, 21]  # if sorted [15, 21, 22, 28]
    print("1.", get_middle_number(numbers1))
    print("2.", get_middle_number(numbers2))

#We are passed a file containing numbers and we must return the number at the middle index
def get_middle_number(numbers):
    numbers.sort()
    return numbers[int(len(numbers) * .5)]

def get_middle_number_from_file(filename):
    op = open(filename, "r")
    #Open the file for reading
    read_file = op.read().split()
    #Read the file and split it on spaces. We now have a list which contains all of our desired numbers
    #however the list also contains a lot of spaces and we do not want those.
    numbers = []
    #Assign a variable to hold the numbers
    for i in range(len(read_file)-1, -1, -1):
    #We will iterate through the list backwards because we want to pop all the space elements in the list
        if read_file[i] == "" or read_file[i] == " ":
        #If the element at the index of the list is a space
            read_file.pop(i)
            #Pop that element
    [numbers.append(int(n)) for n in read_file]
    #Append the remaining elements in the list now into the numbers list we created earlier. Since they came from a file
    #they are of type string so we change the type of each element to int
    numbers.sort()
    return get_middle_number(numbers)
    #Pass our list of numbers from the file to our function which will find the value at the middle index of the list
    #and return that value to us which we will print out.

