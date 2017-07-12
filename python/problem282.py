def eval(stack):
    op = []
    num = []
    i = 0
    while i < len(stack):
        if stack[i] in '+-':
            op.append(stack[i])
        elif stack[i] == '*':
            i += 1
            num.append(num.pop() * int(stack[i]))
        else:
            num.append(int(stack[i]))
        i += 1
    result = num[0]
    for i in range(len(op)):
        if op[i] == '+':
            result += num[i + 1]
        else:
            result -= num[i + 1]
    #print stack, result
    return result

def divide(num):
    results = []
    for i in range(1, len(num)):
        x = num[:i]
        right = num[i:]
        if len(str(int(x))) == i and len(num) - i == len(str(int(right))):
            results.append([x, '+', right])
            results.append([x, '-', right])
            results.append([x, '*', right])
        if len(num) - i > 1:
            for y in divide(right):
                results.append([x, '+'] + y)
                results.append([x, '-'] + y)
                results.append([x, '*'] + y)
    return results

def addOperators(num, target):
    #return divide2(num)
    results = []
    for exp in divide(num):
        if eval(exp) == target:
            results.append(''.join(exp))
    return results
    #return [exp for exp in helper(num) if exp[1] == target]

def test():
    #print addOperators("123", 6)
    #print addOperators("105", 5)
    #print addOperators("00", 0)
    print addOperators("3456237490", 9191)
    #print addOperators("232", 8)

test()
