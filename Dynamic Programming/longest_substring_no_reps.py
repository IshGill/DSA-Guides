# So the intuiton behidn this one! This is a sliding window, it is a dynamic sliding window! What we are doing is this:
# We have a set, of course sets have no repetition, we start form the beginning of the window at windowend which is at the 0th index of the array
# We put the 0th element in our set, we then increment the windowEnd index to expand our window from the beginning and check the 1st index element
# We also update running sum to hold the length of the longest no repeating subarray which in this case will just be one!
# So we are expanding our window, what we are doing is every window expasion we are checking if the element at the end of the window has been seen yet,
# If that end window element has been seen then it is a element in our set, that means we have a repetition, so what we need to do now is move our window along
# so what we do is we remove the first element from our set as this element is repeated in the current index we are looking at! Then we increment our starting window index
# So that the window can move along, we continue to repeat this process and add the largest subarray or window size as the running sum by constantly updating max!
def lengthOfLongestSubstring(s):
    # Starting window index
    windowStart = 0
    # Ending window index
    windowEnd = 0
    # Our running sum which holds the max subarray(window size) which is a set of substring of our string without repetitions
    running_sum = 0
    # Our hash set which will hold the characters without holding any repeats
    hash_set = set()
    while windowEnd < len(s):
        # We need to stop when the end window index reaches the end of the array
        if s[windowEnd] not in hash_set:
            # If the current element we are looking at is not in the set, add it to the set.
            hash_set.add(s[windowEnd])
            # Increase the size of our window
            windowEnd += 1
            # Update the running_sum to hold the new max window size, if the new size is less of course we will stick with the previous max window size of running sum
            running_sum = max(running_sum, len(hash_set))
        else:
            # Else, if we have come across a repetition, this means that the current element we are looking at with s[windowEnd] is already in our hash_set, so we are going to remove the first element
            # in our hash set, thus incrementing our window as we don't want the repeats, we keep doing this until that repeat is gone
            hash_set.remove(s[windowStart])
            # This will make the size of our window smaller
            windowStart += 1
    return running_sum