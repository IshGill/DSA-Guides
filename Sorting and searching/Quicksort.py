def quick_sort(a_list):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = a_list[0]
        less = quick_sort([i for i in a_list if i < pivot])
        greater = quick_sort([i for i in a_list if i > pivot])
        return less + [pivot] + greater

print(quick_sort([7,6,3,99]))
        
