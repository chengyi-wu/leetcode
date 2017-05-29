def printRow(matrix, i, rowStart, rowEnd):
	#print "PRINTROW", i, rowStart, rowEnd
	#offset = 1
	#if rowStart > rowEnd:
	#	offset = -1
	#for j in range(rowStart, rowEnd + offset, offset):
	#	print matrix[i][j],
	if rowStart > rowEnd:
		result = matrix[i][rowEnd:rowStart + 1][:]
		result.reverse()
		return result
	return matrix[i][rowStart:rowEnd + 1]
def printCol(matrix, j, colStart, colEnd):
	#print "PRINT COL", j, colStart, colEnd
	result = []
	offset = 1
	if colStart > colEnd:
		offset = -1
	for i in range(colStart, colEnd + offset, offset):
		result.append(matrix[i][j])
	return result

def spiralOrder(matrix):
	result = []
	rowStart = 0
	colStart = 0
	colEnd = len(matrix) - 1
	rowEnd = len(matrix[0]) - 1

	result = []
	while rowStart != rowEnd and colStart != colEnd:
		result.extend(printRow(matrix, colStart, rowStart, rowEnd))
		colStart += 1
		result.extend(printCol(matrix, rowEnd, colStart, colEnd))
		rowEnd -= 1
		result.extend(printRow(matrix, colEnd, rowEnd, rowStart))
		colEnd -= 1
		result.extend(printCol(matrix, rowStart, colEnd, colStart))
		rowStart += 1
	if rowStart <= rowEnd:
		result.extend(printRow(matrix, colStart, rowStart, rowEnd))
	return result


def test_spiralOrder(matrix):
	print spiralOrder(matrix)

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
