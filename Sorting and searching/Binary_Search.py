# Binary Search: O(log n), cuts the problem size in half each iteration.
def binarySearch(sorted_array, element_to_find):
    min_index = 0
    max_index = len(sorted_array) - 1
    while min_index <= max_index:
        mid = (min_index + max_index) // 2
        if sorted_array[mid] == element_to_find:
            return mid
        elif sorted_array[mid] < element_to_find:
            min_index = mid + 1
        elif sorted_array[mid] > element_to_find:
            max_index = mid - 1
    return -1

print(binarySearch([1,2,3,4,5,6,7,8,9], 7))
