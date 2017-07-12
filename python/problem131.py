def isPalindrome(s):
    for i in range(len(s) / 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def partition(s, memo = { }):
    if s in memo:
        return memo[s]
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
    memo[s] = results
    return results

def test(s):
    results = partition(s)
    print len(results)
    #print results
test("kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu")
test("aab")
test("babb")
test("aabb")
test("bbabb")
