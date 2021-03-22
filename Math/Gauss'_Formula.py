# Gaussian summation formula = n(n + 1)/2 this will give us the sum of all the natural numbers from 0 to n. Beautiful formula.
def missingNumber(self, nums):
    # Remember the Gaussian summation formula! The sum of a sequence is n(n+1)/2
    # This is a beautiful solution. The sum as the gauss formula gives us the sum of n natural numbers and we use that sum to figure out which value is missing as the sum of the nums array is going to give us the sum of n natural numbers also, minus one number from that set of n naturals, and we can easily find that number by taking the difference between the guassian and array sum.
    gauss = len(nums) * (len(nums) + 1) // 2
    num_sum = sum(nums)
    return gauss - num_sum