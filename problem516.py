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
	cache = list(s)
	longest = ""
	memo = { }
	for i in range(len(s)):
		cache[i] = s[i]
		currentLongest = s[i]
		for j in range(i + 1, len(s)):
			cache[j] = cache[j - 1] + s[j]
			if len(cache[j]) > len(longest):
				if isPalindrome(cache[j], memo):
					currentLongest = cache[j]
				elif isPalindrome(currentLongest + s[j], memo):
					currentLongest += s[j]
			if len(longest) < len(currentLongest):
				longest = currentLongest
		#print cache[i:]
	#print memo			
	return longest
	
def test_longestPalindromeSubseq(s):
	print len(s)
	print longestPalindromeSubseq(s)
	
import cProfile
s = "bbbab"
s *= 180
#print s
cProfile.run('test_longestPalindromeSubseq(s)')
#test_longestPalindromeSubseq("bbbabbb")
#test_longestPalindromeSubseq("bbbabb")
#test_longestPalindromeSubseq("cbbd")