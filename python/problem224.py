'''
https://leetcode.com/problems/basic-calculator/#/description
https://leetcode.com/submissions/detail/102844081/
'''

def readNumber(s, i):
	c = 0
	n = 0
	while i < len(s) and s[i] in "0123456789":
		n = n * 10 + int(s[i])
		i += 1
		c += 1
	return (c, n)
def evalstack(s):
	print s
	n = s.pop()
	if n == '-':
		n = 0 - s.pop()
	while len(s) > 0:
		sym = s.pop()
		if sym == "+":
			n += s.pop()
		if sym == '-':
			n -= s.pop()
	return n
def calculate(s):
	stack = []
	i = 0
	while i < len(s):
		#print i, s[i]
		#if s[i] == ' ':
		#	i += 1
		#	continue
		if s[i] in "0123456789":
			c, n = readNumber(s, i)
			stack.append(n)
			i += c
			continue
		if s[i] == '+' or s[i] == '-' or s[i] == '(':
			stack.append(s[i])
		if s[i] == ')':
			symbol = stack.pop()
			substack = [symbol]
			while symbol != '(':
				symbol = stack.pop()
				substack.append(symbol)
			substack.pop()
			stack.append(evalstack(substack))
		i += 1
	print stack
	symbol = stack.pop()
	substack = [symbol]
	while len(stack) > 0:
		substack.append(stack.pop())
	n = evalstack(substack)
	return n
				
def test_calculate(s):
	print calculate(s)		
	
test_calculate(" 2-1 + 2 ")
			