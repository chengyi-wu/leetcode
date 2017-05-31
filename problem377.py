def helper(nums, target, memo):
    #print path, target
    if target in memo:
        return memo[target]
    if target == 0:
        return 1
    if target < 0:
        return 0
    results = 0
    for n in nums:
        results += helper(nums, target - n, memo)
    memo[target] = results
    return results

def combinationSum4(nums, target):
    '''
    Negative number can be allowed provided they have limited number of usages,
    e.g. -1 can only be used at top a few times. Beacuase you can add infinite number of -1
    and add more positive numbers to get a new combination.
    '''
    results = 0
    memo = { }
    for n in nums:
        results += helper(nums, target - n, memo)
    return results

def test():
    print combinationSum4([4,2,1], 32)
    print combinationSum4([1,2,3], 4)

test()
