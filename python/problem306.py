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

def helper(stack, num):
    #print stack, num
    while len(num) > 0:
        print stack, num
        n = str(stack[-1] + stack[-2])
        l = len(n)
        if n == num[:l]:
            stack.append(int(n))
        else:
            return False
        num = num[l:]
    return len(stack) > 2


def isAdditiveNumber2(num):
    '''
    Rewrite the recursion to iteration.
    '''
    for i in range(1, len(num)):
        n = int(num[:i])
        if str(n) == num[:i]:
            stack = [n]
            for j in range(i + 1, len(num)):
                n = int(num[i:j])
                if str(n) == num[i:j] and helper(stack + [n], num[j:]) == True:
                    return True
    return False

def test():
    print isAdditiveNumber2("0235813")
    print isAdditiveNumber2("101")
    print isAdditiveNumber2("1023")
    print isAdditiveNumber2("112358")
    print isAdditiveNumber2("199100199")

test()
