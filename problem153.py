def findMin(nums):
    i = 0
    j = len(nums) - 1
    while i < j and nums[i] > nums[j]:
        print i, j
        m = (i + j) / 2
        if nums[m] > nums[i]:
            i = m
        else:
            j = m
    return nums[i]

def findMin2(nums, i, j):
    print i, j
    if i == j:
        return nums[i]
    if i + 1 == j:
        return min(nums[i], nums[j])
    if nums[i] >= nums[j]:
        m = (i + j) / 2
        if nums[m] > nums[i]:
            return findMin2(nums, m, j)
        if nums[m] < nums[j]:
            return findMin2(nums, i, m)
        return min(findMin2(nums,i, m), findMin2(nums, m, j))
    return nums[i]

def test_findMin(nums):
    return findMin2(nums, 0, len(nums) - 1)

print test_findMin([2,0,1,1,1])
print test_findMin([1,3,3])
print test_findMin([3,5,1])
#print findMin([4,1,2,3])
