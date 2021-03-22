# Bubble sort sorting algorithm works by comparing the element at the current index with the element adjacent to it, hence its direct neighbour.
# If the element which is adjacent is less than the current element, it will swap both elements. This repeats for every single element in the array.
# Therefore, we call it bubble sort because the largest element in each iteration will bubble up to the top of the array.
# We can also note that bubble sort would do the most work on an reverse sorted array such as [7,6,5,4,3,2,1] as it will have to swap every element.
# Important to note that you should have a break statement in case there are no swaps conducted in the inner loop which indicates that the array is now in sorted order, hence, we can return.
# Bubble sort time complexity is O(n^2)
# Bubble sort space complexity is O(1), hence constant auxiliary space usage as everything is indeed happening in place.

def bubbleSort(array):
    for i in range(1, len(array)):
        swap = False
        for n in range(len(array) - 1):
            if array[n] > array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
                swap = True
        if swap == False:
            break
    return array

print(bubbleSort([7, 6, 5, 4, 3, 2, 1]))
