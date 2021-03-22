# 1. Recall XOR properties:
# * a ^ a = 0
# * a ^ 0 = a
# * XOR = True IFF values differ, if equal then False
# 2. So this can be applied nicely to our problem, where we want to find the missing number in an array in O(n) time and O(1) space.
# 3. Let len(nums) = 5 then xor = 5.
# 4. Let nums = [2, 5, 3, 1, 6]
# 4. Then we iterate through every element in nums and what we are doing is building an XOR value our XOR variable will look like this:
# 5. xor = 5 ^ 2 ^ 0 ^ 5 ^ 5 ^ 1 ^ 5 ^ 3 ^ 2 ^ 5 ^ 1 ^ 3 ^ 5 ^ 1 ^ 4 ^ 5 ^ 6 ^ 5
# 6. What we notice here is that every value appears at least twice EXCEPT for 4! Which is the missing value.
# 7. Now due to the property of XOR of a ^ a = 0, all the numbers which appear multiple times will be 0 BUT the other property a ^ 0 = a will also be applied on the number which only appeared once.
# 8. This number which only appears once is the missing value and the XOR operaton will find it as it will do a ^ 0 = a, which will be the remaining value left in the xor variable.
def missingNumber(self, nums):
    xor = len(nums)
    for i in range(len(nums)):
        xor = xor ^ nums[i] ^ i
    return xor