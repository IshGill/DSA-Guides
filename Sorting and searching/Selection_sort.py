# There are two ways to implement selection sort, one is if we sort from top down or bottom down. Both ways have the same principle so your fine with doing it either way, i prefer top down.
# Selection sort will begin iteration from the end of the array, in each iteration it will find the largest element in the unsorted section (which is the entire array at iteration 0)/
# It will swap the largest unsorted element with the first element in the unsorted section of the array which begins at the very end of the array.
# Hence, you can imagine that in each iteration we are building the array from the top down.
# Selection sort time complexity is O(n^2) and auxiliary space usage is O(1), so at least it's nice the it uses constant space.

# Top down, main idea is we go from the end of the list and swap the largest elements
def selectionSort(array):
    for i in range(len(array)-1, -1, -1):
        largest = 0
        for n in range(i + 1):
            if array[n] > array[largest]:
                largest = n
        array[i], array[largest] = array[largest], array[i]
    return array

print(selectionSort([7,6,5,4,3,2,1]))

# Bottom up, main idea is we go from the front of the list and swap the smallest elements
def selectionSortBU(array):
    for i in range(0, len(array)-1):
        smallest = i
        for n in range(i + 1, len(array)):
            if array[n] < array[smallest]:
                smallest = n
        array[i], array[smallest] = array[smallest], array[i]
    return array

print(selectionSortBU([7,6,5,4,3,2,1]))
