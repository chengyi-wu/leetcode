def isPerfectSquare(num):
    '''
    Perfect square is the sum of all the ODD numbers
    '''
    if num < 1:
        return False
    n = 0
    k = 1
    while n < num:
        #print n, k
        n += 2 * k - 1
        k += 1
    return num == n

def test():
    print isPerfectSquare(100)
    #print isPerfectSquare(2147483647)


test()
