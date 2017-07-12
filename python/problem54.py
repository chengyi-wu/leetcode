def getRow(matrix, i, colStart, colEnd):
	#print "getRow", i, colStart, colEnd,
	result = []
	offset = 1
	if colStart > colEnd:
		offset = -1
	for j in range(colStart, colEnd + offset, offset):
		result.append(matrix[i][j])
	#print result
	return result

def getCol(matrix, j, rowStart, rowEnd):
	#print "getCol", j, rowStart, rowEnd,
	result = []
	offset = 1
	if rowStart > rowEnd:
		offset = -1
	for i in range(rowStart, rowEnd + offset, offset):
		result.append(matrix[i][j])
	#print result
	return result

def spiralOrder(matrix):
	result = []
	rowStart = 0
	colStart = 0
	rowEnd = len(matrix) - 1
	if rowEnd < 0:
		return []
	colEnd = len(matrix[0]) - 1

	result = []
	while rowStart < rowEnd and colStart < colEnd:
		result.extend(getRow(matrix, rowStart, colStart, colEnd))
		rowStart += 1
		result.extend(getCol(matrix, colEnd, rowStart, rowEnd))
		colEnd -= 1
		result.extend(getRow(matrix, rowEnd, colEnd, colStart))
		rowEnd -= 1
		result.extend(getCol(matrix, colStart, rowEnd, rowStart))
		colStart += 1

	if rowStart == rowEnd and colStart == colEnd:
		result.append(matrix[rowStart][colStart])
	elif rowStart == rowEnd:
		result.extend(getRow(matrix, rowEnd, colStart, colEnd))
	elif colStart == colEnd:
		result.extend(getCol(matrix, colEnd, rowStart, rowEnd))

	return result[:len(matrix) * len(matrix[0])]


def test_spiralOrder(matrix):
	print spiralOrder(matrix)

test_spiralOrder([[1]])

test_spiralOrder([[1],[2]])

test_spiralOrder([[1,2],[3,4]])

test_spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])

test_spiralOrder([
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ]
])

test_spiralOrder([
 [ 1, 2 ],
 [ 3, 4 ],
 [ 5, 6 ]
])
