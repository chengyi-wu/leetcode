def numDecodings(s, memo):
	#print s
	if s in memo:
		return memo[s]
	if len(s) == 0:
		return 0
	if len(s) == 1:
		if s in "123456789":
			return 1
		return 0
	if len(s) == 2:
		if int(s) < 10:
			return 0
		if int(s) == 10 or int (s) == 20:
			return 1
		if int(s) < 27:
			#memo[s] = 2
			return 2
		if s[1] == "0":
			memo[s] = 0
			return 0
		#memo[s] = 1
		return 1
	n = 0
	if s[0] in "123456789":
		n = numDecodings(s[1:], memo)
		s2 = s[:2]
		if int(s2) < 27:
			n += numDecodings(s[2:], memo)
	memo[s] = n
	return n

import cProfile
s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
#s = "230"
#memo = { }
cProfile.run('print numDecodings(s, { })')
#print memo
