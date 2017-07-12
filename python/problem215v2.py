import random
def findKthLargest(nums, k):
    '''
    Divide & conquer
    Choose a random position, i. Split the arrary into 2 parts. Smaller parts and larger parts
    '''
    print nums, k
    if k > len(nums):
        return None
    #r = len(nums) // 2
    r = random.randint(0, len(nums)- 1)
    x = nums[r]
    print "pivot", x
    small = [n for n in nums if n < x]
    large = [n for n in nums if n > x]
    equal = [n for n in nums if n == x]
    if len(large) >= k:
        return findKthLargest(large, k)
    elif len(large) + len(equal) >= k:
        return x
    return findKthLargest(small, k - len(large) - len(equal))

def test():
    nums = [3,2,1,5,6,4]
    k = 3
    print findKthLargest(nums, k)
    nums = [-1, -1]
    k = 2
    print findKthLargest(nums, k)
    nums = [-1, 2, 0]
    k = 2
    print findKthLargest(nums, k)
    nums = [7,6,5,4,3,2,1]
    k = 2
    print findKthLargest(nums, k)
    nums = [2,1]
    k = 1
    print findKthLargest(nums, k)

test()