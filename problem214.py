def shortestPalindrome(s):
    for i in reversed(range(len(s) + 1)):
        t = s[:i]
        prefix = s[i:]
        print t, t[::-1]
        if t == t[::-1]:
            return prefix[::-1] + s
    return None

def test():
    print shortestPalindrome("aacecaaa")
    print shortestPalindrome("abcd")

test()
