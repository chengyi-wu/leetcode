def strStr(s, pattern):
    '''
    Input: s = random string, p = pattern to match
    Returns the index for the first occurance
    '''
    n = len(s)
    m = len(pattern)
    d = 64
    q = 997
    h = d ** (m - 1) % q
    #print h
    p = 0
    t = 0
    for i in range(m):
        p = (p * d + ord(pattern[i])) % q
        t = (t * d + ord(s[i])) % q
    #print p, t
    for i in range(n):
        print p, t, s[i: i + m]
        if p == t and pattern == s[i:i + m]:
            return i
        elif i < n - m:
            #print s[i], (t - int(s[i]) * h), int(s[i + m]), ((t - int(s[i]) * h) * d + int(s[i + m])) % q
            t = ((t - ord(s[i]) * h) * d + ord(s[i + m])) % q
    return -1

def test():
    s = "chengyiwu1236666666666666666666666666666666666666666666666666666666666666666"
    p = "55555555555555555555wu12366666666666666666666666"
    print strStr(s, p)

test()
