def minSubArrayLen(target, nums):
    min_window_size = 2 ** 31 - 1
    current_window_sum = 0
    window_start = 0
    flag = False
    for window_end in range(len(nums)):
        current_window_sum += nums[window_end]
        while current_window_sum >= target:
            min_window_size = min(min_window_size, window_end - window_start + 1)
            current_window_sum -= nums[window_start]
            window_start += 1
            flag = True
    return min_window_size if flag == True else 0