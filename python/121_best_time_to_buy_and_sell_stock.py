# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            # Find the minimum price.
            minPrice = min(minPrice, prices[i])
            # Compare the current maximum profit with the answer of currentPrice - minimumPrice
            profit = max(profit, prices[i] - minPrice)
        return profit