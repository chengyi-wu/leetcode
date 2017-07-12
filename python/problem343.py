'''
https://leetcode.com/submissions/detail/104627984/
'''

def integerBreak(n, memo = { }):
    if n in memo:
        print n, "HIT"
        return memo[n]
    if n == 1:
        return 1
    p = float("-inf")
    for i in range(1, n / 2 + 1):
        p = max(p, i * integerBreak(n - i), i * (n - i))
    memo[n] = p
    return p

def test_integerBreak(n):
    print n, integerBreak(n)

test_integerBreak(2)
test_integerBreak(10)
