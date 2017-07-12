def longestPalindrome(s, memo = { }):
    if s in memo:
        #print "HIT"
        return memo[s]
    if s == s[::-1]:
        return s
    a = longestPalindrome(s[1:])
    b = longestPalindrome(s[:-1])
    c = longestPalindrome(s[1:-1])
    memo[s] = c
    if len(a) > len(b) and len(a) > len(c):
        memo[s] = a
    if len(b) > len(a) and len(b) > len(c):
        memo[s] = b
    return memo[s]

def longestPalindrome2(s):
    '''
    Walk all the way up from bottom.
    Base case is when i = i, and i = i + 1
    '''
    maxlen = -1
    sub = s
    dp = [False] * len(s)
    for i in reversed(range(len(s))):
        current = dp[:]
        for j in reversed(range(i, len(s))):
            if i == j:
                current[j] = True
            elif i + 1 == j:
                current[j] = s[i] == s[j]
            else:
                current[j] = dp[j - 1] and (s[i] == s[j])
            if current[j] and j - i > maxlen:
                maxlen = j - i
                sub = s[i:j + 1]
        dp = current
    return sub

def longestPalindrome3(s):
    '''
    Walk all the way up from bottom.
    Base case is when i = i, and i = i + 1
    '''
    maxlen = -1
    sub = s
    #dp = [False] * len(s)
    dp = [[False] * len(s)] * len(s)
    for i in reversed(range(len(s))):
        #current = dp[:]
        for j in reversed(range(i, len(s))):
            if i == j:
                dp[i][j] = True
            elif i + 1 == j:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            if dp[i][j] and j - i > maxlen:
                maxlen = j - i
                sub = s[i:j + 1]
        #dp = current
    return sub

def test():
    #print longestPalindrome2("babad")
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    #s = "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"
    #s = "abcda"
    print longestPalindrome2(s)
    print longestPalindrome3(s)

test()
