def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    # Two finger algortihm
    nums1.sort()
    nums2.sort()
    index1 = 0
    index2 = 0
    intersection = []
    while index1 < len(nums1) and index2 < len(nums2):
        if nums1[index1] == nums2[index2]:
            intersection.append(nums1[index1])
            index1 += 1
            index2 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        else:
            index1 += 1
    return intersection

nums1, nums2 = [1,2,2,1], [2,2]
print(intersect(nums1, nums2))
# Output: [2,2]

nums1, nums2 = [4,9,5], [9,4,9,8,4]
print(intersect(nums1, nums2))
# Output: [4,9]