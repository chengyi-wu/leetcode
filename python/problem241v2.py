def readInt(s, i):
	c = 0
	n = 0
	while i < len(s) and s[i].isdigit():
		n = n * 10 + int(s[i])
		c += 1
		i += 1
	return (c, n)

def parseInput(input):
	stack = []
	i = 0
	while i < len(input):
		if input[i].isdigit():
			c, n = readInt(input, i)
			i += c
			stack.append(n)
			continue
		if input[i] in "+-*":
			stack.append(input[i])
		i += 1
	return stack

def helper(stack):
	#print stack
	if len(stack) == 1:
		return stack
	results = []
	for i in range(1, len(stack), 2):
		left = helper(stack[:i])
		op = stack[i]
		right = helper(stack[i + 1:])
		for l in left:
			for r in right:
				if op == '+':
					results.append(l + r)
				if op == '-':
					results.append(l - r)
				if op == '*':
					results.append(l * r)
	return results

def diffWaysToCompute(input):
	stack = parseInput(input)
	#print stack
	return helper(stack)
		
	

#print diffWaysToCompute("15*1*4")
print diffWaysToCompute("2-1-1")
print diffWaysToCompute("2*3-4*5")
print diffWaysToCompute("2")