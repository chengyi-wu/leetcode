import math
def countPrimes(n):
	if n <= 2:
		return 0
	primes = [True] * n
	primes[0] = False
	primes[1] = False
	x = int(math.sqrt(n))
	for i in xrange(x):
		if primes[i]:
			for j in range(i * i, n, i):
				primes[j] = False
	c = 0
	for i in range(n):
		if primes[i]:
			c += 1
	return c

def countPrimes2(n):
	'''
	Runs in linear time
	'''
	if n <= 2:
		return []
	primes = [True] * n
	primes[0] = False
	primes[1] = False
	results = [0] * (n / 2)
	i = 2
	k = 0
	while i < n:
		if primes[i]:
			results[k] = i
			k += 1
		j = 0
		while j < k:
			p = results[j]
			if i * p >= n:
				break
			primes[i * p] = False
			if i % p == 0:
				break
			j += 1
		i += 1
	return k



def test():
	n = 10000000
	print countPrimes2(n)
	print countPrimes(n)

test()
