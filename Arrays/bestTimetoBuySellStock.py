"""
Problem: Best Time to Buy and Sell Stock (At Most One Transaction)
Approach: Single-pass greedy scan; track the minimum price seen so far and compute profit for each day assuming it as a sell day
Time Complexity: O(n) – traverse the price array once
Space Complexity: O(1) – constant extra space
"""


class Solution:
    def maximumProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
