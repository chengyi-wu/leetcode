def longestPalindromeSubseq(s, memo = { }):
	if s in memo:
		return memo[s]
	if len(s) == 0 or len(s) == 1:
		return len(s)
	if s[0] == s[-1]:
		if len(s) == 2:
			return 2
		else:
			memo[s] = 2 + longestPalindromeSubseq(s[1:-1], memo)
			return memo[s]
	memo[s] = max(longestPalindromeSubseq(s[1:], memo), longestPalindromeSubseq(s[:-1], memo))
	return memo[s]

def longestPalindromeSubseq2(s):
	'''
	Same code in C gets accepted and beats 80%, but the python code always failed.
	'''
	size = len(s)
	dp = [0] * (size + 1)
	for i in reversed(range(size)):
		current = dp[:]
		for j in range(size):
			if i == j:
				current[j + 1] = 1
			else:
				if s[i] == s[j]:
					if i + 1 == j:
						current[j + 1] = 2
					else:
						current[j + 1] = 2 + dp[j]
				else:
					current[j + 1] = max(current[j], dp[j + 1])
		dp = current
		#print dp
	return dp[size]


def test_longestPalindromeSubseq(s):
	#print len(s)
	print longestPalindromeSubseq2(s)
	#print longestPalindromeSubseq(s)


s = "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"
#s *= 200
#print s
#s = "bbab"
test_longestPalindromeSubseq(s)
#test_longestPalindromeSubseq("bbbabb")
#test_longestPalindromeSubseq("cbbd")
