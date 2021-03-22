# Insertion sort works by partitioning the array into sorted and unsorted sections.
# Insertion sort will assume the first index in the array is already in sorted order.
# It will be compare the last element in the sorted section with the first unsorted element in the array.
# If the first unsorted element is less than the last sorted element it will swap these two elements, It will then continue to check the unsorted element with all of the elements in the sorted section.
# Once it find a element in the sorted section less than the unsorted element or it hits the 0th index the while loop will break and we place the element there, thus adding it to our sorted section.
# What makes insertion sort useful is the fact that you can add whatever conditions you want to sort the array by, ie you can sort by length, by last letter, literally anything you want and it's quite simple! All you need to d ois specify it in the while loop condition.
# Insertion sort time complexity is O(n^2) and space complexity is O(1) so everything is happening in place.

def insertionSort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and array[i] > value: # Change the condition here in order to sort in respect to a different parameter.
            array[i + 1] = array[i]
            array[i] = value
            i -= 1
    return array

print(insertionSort([7,6,5,4,3,2,1]))

def ReverseinsertionSort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and array[i] < value: # Reverse sort
            array[i + 1] = array[i]
            array[i] = value
            i -= 1
    return array

print(ReverseinsertionSort([7,6,5,4,3,2,1]))


def LengthinsertionSort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and len(array[i]) > len(value): # Length sort string array.
            array[i + 1] = array[i]
            array[i] = value
            i -= 1
    return array

print(LengthinsertionSort(["goku", "vegeta", "gohan", "frieza", "Perfect cell"]))