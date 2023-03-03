// /* Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// # You may assume that each input would have exactly one solution, and you may not use the same element twice.
// # You can return the answer in any order.

// # Example 1:
// # Input: nums = [2,7,11,15], target = 9
// # Output: [0,1]
// # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. */

using System;

namespace twoSumProgram {
class Solution {
    public static int[] twoSum(int[] nums, int target) {
        Dictionary<int, int> hashMap = new Dictionary<int, int>();
        for (int i=0; i<nums.Length; i++) {
            hashMap.Add(nums[i], i);
        }
        for (int i=0; i<nums.Length; i++) {
            int valueRequired = target - nums[i];
            if (hashMap.ContainsKey(valueRequired)) {
                int[] ans = {i, hashMap[valueRequired]};
                return ans;
            }
        }
        return null;
    }

    public static void Main(string[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        int[] res = twoSum(nums, target);
        Array.ForEach(res, i => Console.Write($"{i}, "));
        }
    }
}