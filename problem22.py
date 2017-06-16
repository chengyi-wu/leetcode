'''
https://leetcode.com/problems/generate-parentheses/#/description
'''

def generateParenthesis(n, memo = { }):
    '''
    Top-down solution.
    Generate parenthesis is Catalan series.
    C(n + 1) = SUM(C(k)C(n - k)) for k in range(n)
    '''
    if n in memo:
        return memo[n]
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    results = []
    for k in range(n):
        for a in generateParenthesis(k):
            for b in generateParenthesis(n - 1 - k):
                results.append('(' + a + ')' + b)
    memo[n] = results
    return results

def generateParenthesis2(n):
    '''
    Bottom-up solution. Rewrite for the top-down one. It's faster.
    https://leetcode.com/submissions/detail/106252895/
    '''
    cache = []
    cache.append([''])
    cache.append(['()'])
    for i in range(2, n + 1):
        cache.append([])
        for k in range(i):
            for a in cache[k]:
                for b in cache[i - 1 - k]:
                    cache[i].append('(' + a + ')' + b)
    return cache[n]

def test():
    #print generateParenthesis2(3)
    for n in range(14):
        print n, len(generateParenthesis2(n))

test()
