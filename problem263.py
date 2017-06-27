def isUgly(num):
    print num
    if num <= 0:
        return False
    if num == 1:
        return True
    if num % 2 == 0:
        return isUgly(num / 2)
    if num % 3 == 0:
        return isUgly(num / 3)
    if num % 5 == 0:
        return isUgly(num / 5)
    return False

def test():
    #print isUgly(6)
    #print isUgly(8)
    print isUgly(14)
    #print isUgly(11)
    #print isUgly(100)
    #print isUgly(214797179)

test()
