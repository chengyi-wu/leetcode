def subsetsWithDup(nums):
	nums.sort()
	subsets = [[]]
	for i in range(len(nums)):
		results = []
		for s in subsets:
			if len(s) == 0 or s[-1] != nums[i]: #skipping adding dups
				results.append(s[:])
			results.append(s[:] + [nums[i]])
			#print i, results
		subsets = results
	return subsets
	
print subsetsWithDup([1,2,3])
			