def longestConsecutive(nums):
    h = { }
    m = 0
    for n in nums:
        h[n] = 1
        m = max(n, m)
    i = 0
    currentlen = 0
    maxlen = 0
    while i <= m:
        #print i
        i += 1
        if i not in h:
            currentlen = 0
        else:
            currentlen += h[i]
            maxlen = max(maxlen, currentlen)
    return maxlen


def test():
    print longestConsecutive([2147483647, 4, 200, 1, 3, 2])

test()
