def helper(coins, amount, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    minlen = float('inf')
    for i in xrange(len(coins)):
        minlen = min(minlen, 1 + helper(coins, amount - coins[i], memo))
    memo[amount] = minlen
    return minlen
def coinChange(coins, amount):
    minlen = helper(coins, amount, { })
    #print memo
    if minlen == float('inf'):
        return -1
    return minlen

def coinChange2(coins, amount):
    cache = [float('inf')] * amount + [float('inf')]
    cache[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                cache[i] = min(cache[i], cache[i - c] + 1)
    if cache[amount] == float('inf'):
        return -1
    return cache[amount]

def test():
    #print coinChange([1,2,5], 100)
    #print coinChange2([1,2,5], 100)
    #print coinChange2([1,2147483647], 2)
    print coinChange([313,230,410,263,338,469,431,118,41,221],4906)
    #print coinChange2([313,230,410,263,338,469,431,118,41,221],4906)

test()
