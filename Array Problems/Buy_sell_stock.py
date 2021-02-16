def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    total = 0
    for i in range(len(prices) - 1):
        total += max(prices[i + 1] - prices[i], 0)
    return total

Input = [7,1,5,3,6,4]
print(maxProfit(Input))
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Input = [1,2,3,4,5]
print(maxProfit(Input))
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
Input = [7,6,4,3,1]
print(maxProfit(Input))
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.