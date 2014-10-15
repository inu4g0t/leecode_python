# https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if not prices or len(prices) == 1:
            return 0
        minPrice = prices[0]
        i = 1
        while i < len(prices):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
            i = i + 1
        return profit
