'''
https://leetcode.com/problems/partition-equal-subset-sum/#/description
'''

def helper(left, right, i, nums, memo):
    k = (left, right)
    if k in memo:
        return memo[k]
    #print left, right
    if i == len(nums) :
        #print left, right
        return left == right
    memo[k] = helper(left + nums[i], right - nums[i], i + 1, nums, memo) \
        or helper(left, right, i + 1, nums, memo)
    return memo[k]

def canPartition(nums):
    #nums.sort()
    return helper(0, sum(nums), 0, nums, { })

def test():
    print canPartition([1, 5, 11, 5])
    print canPartition([1, 2, 3, 5])
    print canPartition([1,2,3,4,5,6,7])
    print canPartition([26,50,1,66,5,91,98,65,31,19,15,25,87,58,19,67,64,48,64,85,25,81,7,92,87,6,37,43,8,49,71,47,3,7,10,96,69,78,99,33,91,41,4,34,68,44,100,67,58,57,30,61,100,86,59,65,44,81,82,53,79,48,31,13,39,22,56,43,88,37,66,64,60,27,40,89,99,27,62,50,5,20,31,71,77,14,67,7,44,58,83,96,100,24,86,52,38,31,69,47])
    print canPartition([42,34,32,41,42,66,75,15,53,12,12,88,27,42,19,79,82,59,39,37,47,86,33,89,70,7,75,15,94,74,68,28,66,19,92,97,21,68,59,60,78,60,11,70,8,88,81,58,56,2,36,51,6,85,70,33,3,28,55,62,32,100,70,51,58,84,57,58,14,14,41,98,5,28,61,42,89,7,74,21,13,38,12,73,97,61,92,52,76,66,83,63,20,55,98,15,65,27,95,75])

test()
