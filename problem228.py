def summaryRanges(nums):
    if len(nums) == 0:
        return []
    n = nums[0]
    results = [str(n)]
    for i in xrange(1,len(nums)):
        n += 1
        if n != nums[i]:
            n = nums[i]
            begin = int(results[-1])
            if begin != nums[i - 1]:
                results[-1] += '->' + str(nums[i - 1])
            results.append(str(n))
        elif i == len(nums) - 1:
            results[-1] += '->' + str(nums[i])
    return results

def test():
    nums = [0,1,2,4,5,7]
    print summaryRanges(nums)
    nums = [0,1,2,4,5,6,7]
    print summaryRanges(nums)
    nums = [0]
    print summaryRanges(nums)
    nums = [0,1]
    print summaryRanges(nums)

test()
