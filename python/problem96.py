'''
https://leetcode.com/problems/unique-binary-search-trees/#/description
'''

def numTrees(n, memo):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    results = 0
    for i in range(n):
        left = numTrees(i, memo)
        right = numTrees(n - i - 1, memo)
        results += left * right
    memo[n] = results
    return results

def test_numTrees(n):
    print numTrees(n , { })

test_numTrees(2)
test_numTrees(3)
test_numTrees(4)
test_numTrees(5)
test_numTrees(19)
