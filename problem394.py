def readInteger(s, i):
	n = 0
	c = 0
	while i < len(s) and s[i] in "1234567890":
		n = n * 10 + int(s[i])
		i += 1
		c += 1
	return (c, n)

def decodeString(s):
	stack = []
	i = 0
	while i < len(s):
		if s[i] in "1234567890":
			c, n = readInteger(s, i)
			stack.append(n)
			i += c
			continue
		if s[i] in "abcdefghijklmnopqrstuvwxyz[":
			stack.append(s[i])
		if s[i] == ']':
			sym = stack.pop()
			result = sym
			while sym != '[':
				sym = stack.pop()
				if sym != '[':
					result = sym + result
			
			result *= stack.pop()
			stack.append(result)
		i += 1
	
	result = ""
	for p in stack:
		result = result + p
	return result
	
def test_decodeString(s):
	print decodeString(s)
	
test_decodeString("3[a20[c]]")