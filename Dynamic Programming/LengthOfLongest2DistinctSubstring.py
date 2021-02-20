# Main idea for solving this one is a dynamic sliding window and hash table implementation. Here is the approach.
# 1: Start both the window pointers at the same index
# 2: Every iteration add the current element which the left pointer (the end window pointer) is currently pointing at. This guy is the one that moves down the string!
# 3: Once we have 3 distinct characters in our hash map (remember hash map keys cannot be duplicated!) then this means we need to delete the key of the value seen the longest time ago
# 4: What it means to delete the item seen "longest ago" is simply delete the item in your hash table which has the lowest corresponding string index value, hence the value to the key in the hash map
# 5: Of course, to do this operation with a hash map is simple, find the min value, then index into the corresponding key and do del hash_map[...]
# 6: Once we have deleted this element from the hash map, we now need to change the windows size, hence we need to bring the start of the window up to the point 1 index past the element we just deleted
# 7: So use the same variable (min value variable) and bring your windowStart up accordingly
# 8: Finally we do a check everytime to see if we have the longest distance between our string values which contain only 2 distinct characters, we add 1 to get the length between them.
def lengthOfLongestSubstringTwoDistinct(s):
    hash_map = {}
    windowStart = 0
    windowEnd = 0
    maxLen = 0
    while windowEnd < len(s):
        hash_map[s[windowEnd]] = windowEnd
        if len(hash_map) >= 3:
            find_min = min(hash_map.values())
            del hash_map[s[find_min]]
            windowStart = find_min + 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
        windowEnd += 1
    return maxLen

print(lengthOfLongestSubstringTwoDistinct("eceba"))