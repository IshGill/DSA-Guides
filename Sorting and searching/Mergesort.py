def mergesort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2  # Finding the mid of the array
        left_sublist = a_list[:mid]  # Dividing the array elements
        right_sublist = a_list[mid:]  # into 2 halves
        mergesort(left_sublist)  # Sorting the first half
        mergesort(right_sublist)  # Sorting the second half
        small_unsort_left = small_unsort_right = main_list_pos = 0

# Copy data to temp arrays L[] and R[]
        while small_unsort_left < len(left_sublist) and small_unsort_right < len(right_sublist):
            if left_sublist[small_unsort_left] < right_sublist[small_unsort_right]:
                a_list[main_list_pos] = left_sublist[small_unsort_left]
                small_unsort_left += 1
            else:
                a_list[main_list_pos] = right_sublist[small_unsort_right]
                small_unsort_right += 1
            main_list_pos += 1

    # Checking if any element was left
        while small_unsort_left < len(left_sublist):
            a_list[main_list_pos] = left_sublist[small_unsort_left]
            small_unsort_left += 1
            main_list_pos += 1
        while small_unsort_right < len(right_sublist):
            a_list[main_list_pos] = right_sublist[small_unsort_right]
            small_unsort_right += 1
            main_list_pos += 1
    return a_list

print(mergesort([8, 7, 6, 5, 4, 3, 2, 1]))