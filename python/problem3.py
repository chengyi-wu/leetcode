def lengthOfLongestSubstring(s):
    h = {}
    longest = 0
    sub = 0
    for i, c in enumerate(s):
        if i > 0:
            if c in h:
                sub = i - h[c]
                new_map = {}
                for k in h:
                    if h[k] > h[c]:
                        new_map[k] = h[k]
                h = new_map
            else:
                sub += 1
        else:
            sub = 1
        h[c] = i
        longest = max(longest, sub)

    return longest
        

s = ["abba", 'abcabc', 'pwwkew', "wobgrovw"]
for tests in s:
    print(lengthOfLongestSubstring(tests))