'''
Problem: https://leetcode.com/problems/gray-code/#/description
'''
def helper(n):
	'''
	When leading digit is 1, it's the exact reverse when the leading digit is 0.
	Observe when 3 is the case:
		0 00
		0 01
		0 11
		0 10
		
		1 10
		1 11
		1 01
		1 00
	'''
	if n == 1:
		return ["0", "1"]
	results = []
	temp = helper(n - 1)
	for p in temp:
		results.append("0" + p)
	temp.reverse()
	for p in temp:
		results.append("1" + p)
	return results

def getGreyCode(n):
	if n == 0:
		return [0]
	results = []
	for c in helper(n):
		#print c
		results.append(int(c,2))
	return results
	
print getGreyCode(int(raw_input()))