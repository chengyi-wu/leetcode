def isPalindrome(s):
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def partition(s):
    if len(s) == 1:
        return [[s]]
    results = []
    if isPalindrome(s):
        results.append([s])
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        if isPalindrome(left):
            right = partition(s[i:])
            for r in right:
                results.append([left] + r)
    return results

def test(s):
    results = partition(s)
    print len(results)
    print results

print test("aab")
print test("babb")
print test("aabb")
print test("bbabb")
