# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            # If we can make a profit by buying at the previous day and selling on the next day, then do the transaction.
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit