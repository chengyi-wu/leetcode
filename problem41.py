def firstMissingPositive(nums):
    if 0 not in nums:
        nums.append(0)
    big = { }
    small = { }
    h = []
    for n in nums:
        big[n] = None
        small[n] = None
    for n in nums:
        if n - 1 in small:
            small[n] = n - 1
        if n + 1 in big:
            big[n] = n + 1
    segment = []
    missing = []
    for n in nums:
        if n not in h:
            s = [n]
            x = small[n]
            h.append(n)
            while x != None:
                s = [x] + s
                h.append(x)
                x = small[x]
            x = big[n]
            while x != None:
                s = s + [x]
                h.append(x)
                x = big[x]
            segment.append(s)
    for s in segment:
        left = s[0]
        right = s[-1]
        if left - 1 > 0:
            missing.append(left - 1)
        if right + 1 > 0:
            missing.append(right + 1)
    return min(missing)

def test():
    nums = [1,2,0]
    print firstMissingPositive(nums)
    nums = [3,4,-1,1]
    print firstMissingPositive(nums)

test()
