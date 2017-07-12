'''
https://leetcode.com/problems/pascals-triangle/#/description
https://leetcode.com/problems/pascals-triangle-ii/#/description
'''

def generate(numRows):
	result = []
	for i in range(numRows):
		result.append([1])
		for j in range(1, i):
			result[i].append(result[i - 1][j - 1] + result[i - 1][j])
		if i > 0:
			result[i].append(1)
	return result[-1]
	
def test_generate():
	'''
	PROBLEM119
	'''
	print generate(int(raw_input()) + 1)

test_generate()