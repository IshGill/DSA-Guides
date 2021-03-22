def countBits(self, nums):
    return [len(bin(i)[2:].replace("0", "")) for i in range(nums + 1)]