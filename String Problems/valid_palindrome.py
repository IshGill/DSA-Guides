def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = "".join([i.lower() for i in s if i.isalnum()])
    if len(s) == 0:
        return True
    count = -1
    for i in range(len(s)):
        if s[i] == s[count]:
            count -= 1
        else:
            return False
    return True

Input = "A man, a plan, a canal: Panama"
print(isPalindrome(Input))
# Output: true