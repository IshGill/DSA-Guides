# Recursive implementation of binary search. O(log n) runtime as problem is cut in half but uses extra space for recursive call stack.
def recursiveBS(min_index, max_index, element_to_find, array):
    index = 0
    if min_index > max_index:
        return -1
    else:
        mid = (min_index + max_index) // 2
        if array[mid] == element_to_find:
            index = mid
            return index
        elif array[mid] < element_to_find:
            index = recursiveBS(mid + 1, max_index, element_to_find, array)
        elif array[mid] > element_to_find:
            index = recursiveBS(min_index, mid - 1, element_to_find, array)
    return index


def findIndex(array, element_to_find):
    return recursiveBS(0, len(array)-1, element_to_find, array)

print(findIndex([1,2,3,4,5,6,7,8,9], 7))
