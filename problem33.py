def binarySearch(a, i, j, target):
	while i < j and i + 1 != j:
		k = (i + j) / 2
		#print k, a[k], i , j
		if a[k] > target:	
			j = k
		if a[k] < target:
			i = k
		if a[k] == target:
			return k
		
	if a[i] == target:
		return i
	if a[j] == target:
		return j
	return -1

def search(nums, target):
	print nums, target
	i = 0
	j = len(nums) - 1
	a = nums[:]
	if a[i] < a[j]:
		return binarySearch(nums, 0, j, target)
	while a[i] > a[j] and i != j and i + 1 != j:
		k = (i + j) / 2
		#print i, j, k
		if a[k] > a[i]:
			i = k
		if a[k] < a[j]:
			j = k
	# j is the shift
	if a[0] > target:
		return binarySearch(nums, j, len(nums) - 1, target)
	else:
		return binarySearch(nums, 0, j - 1, target)
	
	

print search([5, 6, 7, 8, 0, 1, 2, 3, 4], 7)
	
print search([1,3,5,7], 1)
print search([1,3,5,7], 0)
print search([1,3,5,7], 2)
print search([1,3,5,7], 4)
print search([1,3,5,7], 7)