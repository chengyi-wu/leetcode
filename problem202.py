def isHappy(n):
    path = [n]
    while True:
        s = 0
        while n > 0:
            d = n % 10
            s += d * d
            n /= 10
        print s
        if s == 1:
            return True
        if s in path:
            break
        else:
            path.append(s)
        n = s
    return False

def test():
    print isHappy(19)
    print isHappy(2)
    print isHappy(1111111)

test()
