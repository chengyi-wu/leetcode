def doCompute(s):
	print "\tdoCompute", s
	if s[1] == '+':
		return int(s[0]) + int(s[2])
	if s[1] == '-':
		return int(s[0]) - int(s[2])
	if s[1] == '*':
		return int(s[0]) * int(s[2])
	return 0

def diffWaysToCompute(input):
	#print input
	if len(input) == 1:
		#print input
		return [int(input)]
	if len(input) == 3:
		return [doCompute(input)]
	results = []
	for i in range(0, len(input) - 1, 2):
		s = input[i:i+3]
		#print s
		v = str(doCompute(s))
		results.extend(diffWaysToCompute(input[:i] + v + input[i + 3:]))
	return results
		
print diffWaysToCompute("2-1-1")
print diffWaysToCompute("2*3-4*5")