'''
https://leetcode.com/problems/maximum-product-subarray/#/description

https://leetcode.com/submissions/detail/102833797/
'''

def maxProductWithMemo(p, i, nums, memo):
	'''
	Unfortunately, this code won't work if len(nums) is very long. 
	It'll exceed the max recursion depth. 
	Neverthless, it works for most of the cases
	'''
	print i
	k = (p, i)
	if k in memo:
		return memo[k]
	while i < len(nums) and nums[i] == 1:
		i += 1
	while i < len(nums) and p > 0 and nums[i] == -1:
		i += 1
	if i == len(nums):
		return p
	taking = maxProductWithMemo(p * nums[i], i + 1, nums, memo)
	nontaking = maxProductWithMemo(nums[i], i + 1, nums, memo)
	memo[k] = max(taking, nontaking)
	memo[k] = max(p, memo[k])
	return memo[k]
def maxProduct(nums):
	memo = { }
	r = maxProductWithMemo(nums[0], 1, nums, memo)
	print memo
	return r

def maxProduct2(nums):
	'''
	This looks like black magic.
	Two arrays: 
		One stores the max product so far. 
		The other stores the min product so far. It's used when there're neg values. 
		Since the max product can also be accquired by two negs.
	'''
	maxProduct = nums[0]
	p = nums[:] #max product so far
	neg = nums[:] #neg's min so far. If none, stores nums[i] itself.
	for i in range(1, len(nums)):
		v1 = nums[i] * p[i - 1]
		v2 = nums[i] * neg[i - 1]
		m1 = max(v1, v2)
		m2 = min(v1, v2)
		neg[i] = min(nums[i], m2)
		p[i] = max(nums[i], m1)
		maxProduct = max(maxProduct, p[i])
		#p[i] = max(p[i - 1], p[i])
		print i, p[i], neg[i]
	return maxProduct
			

import cProfile
print maxProduct2([-2,0,-1])
print maxProduct2([2,3,-2,4])
print maxProduct2([-2,1,-3,4,-1,2,1,-5,4])
cProfile.run('print maxProduct2([-5,2,4,1,-2,2,-6,3,-1,-1,-1,-2,-3,5,1,-3,-4,2,-4,6,-1,5,-6,1,-1])')
print maxProduct2([2,3,-4,5,6])