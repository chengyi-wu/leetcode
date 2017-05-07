import math

def permute(nums):
	if len(nums) == 1:
		return [str(nums[0])]
	results = []
	for i in xrange(len(nums)):
		for p in permute(nums[:i] + nums[i + 1:]):
			results.append(str(nums[i]) + p)
			
	return results
	
	
def getPermutation(n, k):
	f = { 1:1, 2:2, 3:6, 4:24 }
	digits = range(1,n + 1)
	print digits
	while k > 0:
		d = int(math.ceil(float(k) / f[n -1]))
		
		print int(d), k, f[n], k % f[n - 1]
		#digits.remove(d)
		k %= f[n - 1]
		n -= 1
	print digits
		
results = permute([1,2,3])
for i, p in enumerate(results):
	print i + 1, p
	
results = permute([1,2,3,4])
for i, p in enumerate(results):
	print i + 1, p
			
print getPermutation(3, 1)	
#print getPermutation(3, 2)
#print getPermutation(3, 3)
#print getPermutation(3, 4)
