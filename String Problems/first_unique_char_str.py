def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return -1
    if len(s) == 1:
        return 0
    hash_table = {}
    for i in s:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1
    for i in s:
        if hash_table[i] <= 1:
            return s.find(i)
    return -1

s = "leetcode"
print(firstUniqChar(s))
# return 0.

s = "loveleetcode"
print(firstUniqChar(s))
# return 2.