def helper(s, i, nums, k, memo):
	t = (i, s)
	print t
	if t in memo:
		print "HIT"
		return memo[t]
	if len(nums) == i:
		return s % k == 0
	
	taking = helper(s + nums[i], i + 1, nums, k, memo)
	if taking == True:
		return True
	nontaking = helper(nums[i], i + 1, nums, k, memo)
	if nontaking == True:
		return True
	memo[t] = False
	return False
	
	
def checkSubarraySum(nums, k):
	return helper(0, 0, nums, k, { })
	
print checkSubarraySum([23, 2, 4, 6, 7], 13)

print checkSubarraySum([23, 2, 6, 4, 7], 42)
	