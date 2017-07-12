def helper(prices, i, memo):
    if i in memo:
        return memo[i]
    profit = 0
    for j in range(i, len(prices)):
        profit = max(profit, prices[j] - prices[i] + helper(prices, j + 1, memo))
    memo[i] = profit
    print prices[i:], profit
    return profit

def maxProfit(prices):
    '''
    This time out as well as STACK OVERFLOW
    '''
    maxProfit = 0
    memo = { }
    for i in range(len(prices)):
        maxProfit = max(helper(prices, i, memo), maxProfit)
    return maxProfit

def maxProfit2(prices):
    profits = prices[:]
    for i in range(len(prices)):
        if i == 0:
            profits[i] = 0
        else:
            profits[i] = max(0, prices[i] - prices[i - 1])
    return sum(profits)

def test_maxProfit(prices):
    print maxProfit2(prices)

test_maxProfit([3,2,6,5,0,3])
