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

def longestConsecutive2(nums):
    small = { }
    big = { }
    for n in nums:
        small[n] = None
        big[n] = None
    for k in nums:
        if k - 1 in small:
            small[k] = k - 1
        if k + 1 in big:
            big[k] = k + 1
    #h = { }
    h = []
    maxlen = 0
    #print small,big
    for n in nums:
        currentlen = 1
        if n not in h:
            x = small[n]
            while x != None:
                currentlen += 1
                #h[x] = True
                h.append(x)
                x = small[x]
            x = big[n]
            while x != None:
                currentlen += 1
                #h[x] = True
                h.append(x)
                x = big[x]
        maxlen = max(maxlen, currentlen)
    return maxlen

def test():
    print longestConsecutive2([2147483647, 4, 200, 1, 3, 2])

test()
