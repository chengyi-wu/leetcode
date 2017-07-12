def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    indexes = [0] * len(primes)
    k = 1
    numbers = [1]
    while k != n:
        candidates = []
        for i, p in enumerate(primes):
            candidates.append(numbers[indexes[i]] * p)
        un = min(candidates)
        for i, x in enumerate(candidates):
            if un == x:
                indexes[i] += 1
        #print candidates
        numbers.append(un)
        k += 1
    return numbers[-1]

def test():
    primes = [2, 7, 13, 19]
    for i in range(1, 100):
        print i, nthSuperUglyNumber(i, primes)

test()
