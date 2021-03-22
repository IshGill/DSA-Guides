def findMedianSortedArrays(nums1, nums2):
    new_nums = []
    # Edge cases
    if len(nums1) == 0 and len(nums2) == 0:
        return []
    elif len(nums1) == 0 and len(nums2) != 0:
        new_nums = nums2
    elif len(nums2) == 0 and len(nums1) != 0:
        new_nums = nums1
    else:
        new_nums = nums1 + nums2

    if len(new_nums) == 1:
        return float(new_nums[0])
    new_nums.sort()
    mid = (0 + len(new_nums) - 1) // 2
    if len(new_nums) % 2 != 0:
        return new_nums[mid]
    else:
        return (new_nums[mid + 1] + new_nums[mid]) / 2.0