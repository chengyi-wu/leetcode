def helper(nums, k):
	#print nums[0], k
	results = []
	if k == 1:
		for n in nums:
			results.append([n])
		return results
	#results = []
	for i in xrange(len(nums) - k + 1):
		n = nums[i]
		for c in helper(nums[i+1:], k - 1):
			results.append(c[:] + [n])
	return results
	
def combine(n, k):
	nums = range(n, 0, -1)
	
	return helper(nums, k)
	
import cProfile
cProfile.run('combine(20, 16)')