def get_merge_list(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + get_merge_list(alist[1:])

print(get_merge_list([[1, 2, 3], [2, 3, 5, 6], [7, 8, 9]]))
