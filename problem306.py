def isAdditiveNumber(path, num):
    print path, num
    if len(num) == 0:
        return len(path) > 2
    for i in range(1, len(num) + 1):
        if len(path) > 1:
            v = str(path[-1] + path[-2])
            #print v, num[:i + len(v)]
            if v == num[:len(v)]:
                if isAdditiveNumber(path + [int(v)], num[len(v):]):
                    return True
            else:
                return False
        elif isAdditiveNumber(path + [int(num[:i])], num[i:]):
            return True
    return False

def test():
    print isAdditiveNumber([], "112358")
    print isAdditiveNumber([], "199100199")

test()
