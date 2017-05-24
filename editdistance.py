'''
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-21-dp-iii-parenthesization-edit-distance-knapsack/

INSERT/DELTE/REPLACE count as 1

For string X and Y, if X[i] and Y[j] are different, the operation would be to INSERT Y[j] to X[i] or REMOVE Y[j] or REPLACE X[i] with Y[j]
'''

def minDistance(word1, word2, memo = { }):
    #print word1, word2
    k = (word1, word2)
    if k in memo:
        return memo[k]
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)
    if word1[0] != word2[0]:
        memo[k] = 1 + min(minDistance(word1, word2[1:], memo), minDistance(word1[1:], word2, memo),minDistance(word1[1:], word2[1:], memo))
    else:
        memo[k] =  minDistance(word1[1:], word2[1:], memo)
    return memo[k]

def test_minDistance(word1, word2):
    print minDistance(word1, word2)

test_minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine")
