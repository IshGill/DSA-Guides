def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    return [s.insert(0, s.pop(i)) for i in range(len(s))]

Input = ["h","e","l","l","o"]
print(reverseString(Input))
# Output: ["o","l","l","e","h"]