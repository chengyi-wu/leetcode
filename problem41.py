def firstMissingPositive2(nums):
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
            left = s[0] - 1
            right = s[-1] + 1
            if left > 0:
                missing.append(left)
            if right > 0:
                missing.append(right)
    return min(missing)

def firstMissingPositive(nums):
    nums.append(0)
    for i in range(len(nums)):
        #print i, nums[i], nums[i] - 1
        pos = nums[i]
        while pos >= 0 and pos < len(nums) and pos != nums[pos]:
            t = nums[pos]
            nums[pos] = pos
            pos = t
        print nums
    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)

def test():
    nums = [1,2,0]
    print firstMissingPositive(nums)
    nums = [3,4,-1,1]
    print firstMissingPositive(nums)

test()
