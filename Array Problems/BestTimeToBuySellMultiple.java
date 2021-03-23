package Leetcode.ArrayProblems;

public class BestTimeToBuySellMultiple {
    /* Look idea is super straight forward! I want to buy every day and sell every day BUT if I sell for a loss just add 0! It's a glitch in the system lol. */
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            max_profit += Math.max(prices[i + 1] - prices[i], 0);
        }
        return max_profit;

    }
}

