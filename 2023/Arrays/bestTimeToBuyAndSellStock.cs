using System;

namespace BestTimeToBuyAndSellStock {
    class Solution {
        static int maxProfit(int[] nums) {
            int minVal, maxVal, maxProfit;
            minVal = maxVal = nums[0];
            maxProfit = 0;
            for (int i=1; i<nums.Length; i++) {
                if (nums[i] < minVal) {
                    minVal = nums[i];
                    maxVal = nums[i];
                }
                else {
                    maxVal = Math.Max(maxVal, nums[i]);
                }
                maxProfit = Math.Max(maxProfit, maxVal - minVal);
            }
            return maxProfit; 
        }

        static void Main(string[] args) {
            int[] prices = {7,1,5,3,6,4};
            int ans = maxProfit(prices);
            Console.WriteLine(ans);
        }
    }
}