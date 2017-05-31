def helper(path, nums, k, n):
    #print path, k, n
    if k == 0:
        if n == 0:
            return [path]
        return []
    results = []
    for i in range(len(nums)):
        results.extend(helper(path + [nums[i]],nums[i + 1:], k - 1, n - nums[i]))
    return results

def combinationSum3(k, n):
    nums = [x for x in range(1, 10)]
    results = []
    for i in range(len(nums)):
        results.extend(helper([nums[i]], nums[i + 1:], k - 1, n - nums[i]))
    return results

def test():
    print combinationSum3(3, 9)
    print combinationSum3(3, 7)

test()
