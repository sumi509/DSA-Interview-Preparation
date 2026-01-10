"""
Problem: Best Time to Buy and Sell Stock (LeetCode #121)

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell.

Approach:
Keep track of the minimum price so far and calculate profit at each step.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example
prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5
