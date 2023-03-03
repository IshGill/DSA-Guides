# Algorithm: BINARY SEARCH

def binary_search(sorted_list, n):
    min_idx = 0
    max_idx = len(sorted_list) - 1
    while max_idx >= min_idx:
        mid = (min_idx + max_idx) // 2
        if sorted_list[mid] == n:
            return mid
        elif sorted_list[mid] > n:
            max_idx = mid - 1
        elif sorted_list[mid] < n:
            min_idx = mid + 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([1], 1))
print(binary_search([], 5))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))

# Runtime: O(log n)

