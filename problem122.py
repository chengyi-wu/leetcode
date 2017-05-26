def helper(prices, i, memo):
    if i in memo:
        return memo[i]
    profit = 0
    for j in range(i + 1, len(prices) - 1):
        profit = max(profit, prices[j] - prices[i] + helper(prices, j + 1, memo))
    memo[i] = profit
    return profit

def maxProfit(prices):
    maxProfit = 0
    memo = { }
    for i in range(len(prices) - 1):
        maxProfit = max(helper(prices, i, memo), maxProfit)
    return maxProfit

def test_maxProfit(prices):
    print maxProfit(prices)

test_maxProfit([7,1,5,3,6,4])
