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
		
	i = 0
	j = nRow - 1
	while matrix[i][0] < matrix[j][0] and i != j and i + 1 != j:
		k = (i + j) / 2
		if matrix[k][0] > target:
			j = k
		if matrix[k][0] < target:
			i = k
		if matrix[k][0] == target:
			return True
			
	if binarySearch(matrix[i], 0, nCol - 1, target) != -1:
		return True
	if binarySearch(matrix[j], 0, nCol - 1, target) != -1:
		return True
	return False
	
print searchMatrix([[1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 34)