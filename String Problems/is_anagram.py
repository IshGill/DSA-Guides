def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return sorted(s) == sorted(t)

s, t = "anagram", "nagaram"
print(isAnagram(s,t))
# Output: true