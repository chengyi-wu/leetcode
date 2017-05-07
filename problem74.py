'''
https://leetcode.com/problems/search-a-2d-matrix/#/description
'''

def binarySearch(a, i, j, target):
	print a, i, j, target
	while i < j and i + 1 != j:
		k = (i + j) / 2
		if a[k] == target:
			return k
		if a[k] > target:
			j = k
		if a[k] < target:
			i = k
	if a[i] == target:
		return i
	if a[j] == target:
		return j
	return -1
	
def searchMatrix(matrix, target):
	nRow = len(matrix)
	if nRow == 0:
		return False
	nCol = len(matrix[0])
	if nCol == 0:
		return False
		
	for i in xrange(nRow):
		if matrix[i][0] == target:
			return True
		if matrix[i][0] > target:
			if i == 0:
				return False
			if binarySearch(matrix[i - 1], 0, nCol - 1, target) != -1:
				return True
			return False
	if matrix[nRow - 1][nCol - 1] >= target:
		if binarySearch(matrix[i], 0, nCol - 1, target) != -1:
			return True
	return False
	
print searchMatrix([[1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 34)