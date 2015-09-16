# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profitL = []
        profitR = []
        profit = 0
        # Go from left to right to get the max profit from 0 to i, stored into profitL.
        minPrice = prices[0]
        for i in prices:
            minPrice = min(minPrice, i)
            profit = max(profit, i - minPrice)
            profitL.append(profit)

        # Go from right to left, get the max profit from n to i, stored into profitR
        profit = 0
        maxPrice = prices[-1]
        for i in reversed(prices):
            maxPrice = max(maxPrice, i)
            profit = max(profit, maxPrice - i)
            profitR.insert(0, profit)

        # The final profit equals to the sum of the max profit of the two sides.
        maxProfit = profitL[-1] 
        for i in range(len(prices) - 1): 
            maxProfit = max(maxProfit, profitL[i] + profitR[i + 1])
        return maxProfit
        