def bsearch(s, nums, windowSize):
    '''
    Helper function to determine if the windowSize is good.
    :type s: int
    :type nums: List[int]
    :type windowSize: int
    :rtype: bool
    '''
    val = sum(nums[:windowSize])
    if val >= s:
        return True
    for i in xrange(len(nums) - windowSize):
        val = val - nums[i] + nums[i + windowSize]
        if val >= s:
            return True
    #print "bsearch", windowSize, False
    return False

def minSubArrayLen(s, nums):
    '''
    https://leetcode.com/problems/minimum-size-subarray-sum/
    Use binary search for a windowSize. O(nlogn)
    :type s: int
    :type nums: List[int]
    :rtype: int
    '''
    windowSize = len(nums)
    if windowSize == 0:
        return 0
    low = 1
    high = windowSize

    while low != high:
        m = (low + high) // 2

        if bsearch(s, nums, m):
            high = m - 1
        else:
            low = m + 1
    if bsearch(s, nums, low):
        return low
    elif low == len(nums):
        return 0
    return low + 1

def minSubArrayLenN(s, nums):
    '''
    Use a pointer in the front to keep track of the start position
    O(N)
    '''
    val = nums[0]
    if val >= s:
        return 1
    minLen = float('inf')
    front = 0
    for i in xrange(1, len(nums)):
        val += nums[i]    
        while val >= s:
            size = i - front + 1
            minLen = min(minLen, size)
            val -= nums[front]
            front += 1
    if minLen == float('inf'):
        return 0
    return minLen

def test():
    s = 7
    nums = [2,3,1,2,4,3] 
    print minSubArrayLenN(s, nums)
    print minSubArrayLen(s, nums)

    s = 11
    nums = [1,2,3,4,5]
    print minSubArrayLenN(s, nums)
    print minSubArrayLen(s, nums)

if __name__ == '__main__':
    test()