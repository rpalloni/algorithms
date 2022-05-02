# Find the maximum profit with stock prices for a number of minutes forward.
# Each minute you can buy ONE share, sell N shares or nothing.
# prices: an array of n integers that denote the stock prices at minutes 1 through n.

# For example, if predicted prices over the next n = 6 minutes are prices = [3, 4, 5, 3, 5, 2],
# one way to maximize profit is to purchase a share in each of the first 2 minutes for cash flows -3 + -4 = -7,
# then sell them at the 3rd minute for 2 * 5 = 10. Purchase a share in the 4th minute for 3 and sell it in the 5th minute for 5.
# Total profit is: -3 - 4 + 10 - 3 + 5 = 5

prices0 = [1, 2, 100] # 3 minutes
prices1 = [1, 3, 1, 2] # 4 minutes
prices2 = [3, 4, 5, 3, 5, 2] # 6 minutes

# version 1
def max_profit(prices):
    m = prices.pop() # get last
    maxsum = 0
    arrsum = 0
    for p in reversed(prices):
        m = max(m, p)
        maxsum += m
        arrsum += p
    return maxsum-arrsum

max_profit(prices0)
max_profit(prices1)
max_profit(prices2)

# version 2
def maximumProfit(prices):
    profit = 0
    max_price = 0
    for p in reversed(prices):
        if max_price <= p:
            max_price = p
        profit += (max_price - p)
    return profit

maximumProfit(prices0)
maximumProfit(prices1)
maximumProfit(prices2)
