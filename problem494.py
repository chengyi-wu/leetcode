import cProfile
def findTargetSumWays(i, nums, S, memo):
	k = (i, S)
	if k in memo:
		return memo[k]
	if i == len(nums):
		if S == 0:
			return 1
		else:
			return 0
	n = findTargetSumWays(i + 1, nums, S - nums[i], memo)
	n += findTargetSumWays(i + 1, nums, S + nums[i], memo)
	memo[k] = n
	return n

def test_findTargetSumWays():
	
	cProfile.run('n = findTargetSumWays(0, [1, 1, 1, 1, 1], 3, { })')
	print n
test_findTargetSumWays()