package Leetcode.ArrayProblems;

public class MaximumSubArray {
        public int maxSubArray(int[] nums) {
        int currMax = nums[0]; int globalMax = nums[0];
        for (int i = 1; i < nums.length; i++) {
            currMax = Math.max(nums[i], nums[i] + currMax);
            globalMax = Math.max(globalMax, currMax);
        }
        return globalMax;
    }
}

