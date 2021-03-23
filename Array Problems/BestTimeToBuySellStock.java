package Leetcode.ArrayProblems;

/* Simple straight forward problem
1. Don't make the mistake of looking for the MAX value to sell at and focusing entirely on that! The key here is the min_val.
2. Why min val? Because what's the point in finding the highest price to sell at if you already have a really high buy price?
3. You should look for BOTH the lowest price to buy at and highest price to sell at!
4. That's why the min_val update is there, because if our current value is cheaper than our previous value which we bought at we should update! And take that discounted price!
5. Keep this in mind! For these stock problems don't always go for the max price to sell consider both!
6. Time complexity is O(n), space complexity is O(1).
 */
public class BestTimeToBuySellStock {
    public int maxProfit(int[] prices) {
        int min_val = prices[0];
        int max_profit = 0;
        for (int i = 1; i < prices.length; i++) {
            max_profit = Math.max(max_profit, prices[i] - min_val);
            min_val = Math.min(min_val, prices[i]);
        }
        return max_profit;
    }
}

