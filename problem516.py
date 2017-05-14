def isPalindrome(s, memo):
	if s in memo:
		return memo[s]
	for i in range(len(s)/2 + 1):
		if s[i] != s[len(s) - 1 - i]:
			memo[s] = False
			return False
	memo[s] = True
	return True

def longestPalindromeSubseq(s):
	cache = []
	for c in s:
		cache.append(c)
	longest = ""
	memo = { }
	for i in range(len(s)):
		cache[i] = s[i]
		for j in range(i + 1, len(s)):
			cache[j] = cache[j - 1] + s[j]
			if len(cache[j]) > len(longest):
				if isPalindrome(cache[j], memo):
					longest = cache[j]
				elif isPalindrome(longest + s[j], memo):
					longest += s[j]
		#print cache[i:]
	print memo			
	return longest
	
def test_longestPalindromeSubseq(s):
	print longestPalindromeSubseq(s)
	
test_longestPalindromeSubseq("bbabbb")
test_longestPalindromeSubseq("bbbabbb")
test_longestPalindromeSubseq("bbbabb")
test_longestPalindromeSubseq("cbbd")