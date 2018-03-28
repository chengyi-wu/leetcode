def getScrambles(s, cache):
    if len(s) == 0 or len(s) == 1:
        return [s]
    if s in cache:
        print('hit', s)
        return cache[s]
    print(s)
    ret = []
    for i in range(len(s) - 1):
        left = s[:i + 1]
        right = s[i + 1:]
        for l in getScrambles(left, cache):
            for r in getScrambles(right, cache):
                ret.append(l + r)
                ret.append(r + l)

    cache[s] = ret
    return ret

def isScramble(s1, s2):
    cache = {}
    scrambles = getScrambles(s1, cache)
    print(cache)
    print(scrambles)
    return  s2 in scrambles

print(isScramble('rgtae', 'great'))
print(isScramble("abcdefghijklmn", "efghijklmncadb"))
