def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if len(digits) == 0:
        return digits
    digits = "".join([str(i) for i in digits])
    digits = int(digits) + 1
    return [int(i) for i in str(digits)]

digits = [1,2,3]
print(plusOne(digits))
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

digits = [4,3,2,1]
print(plusOne(digits))
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.