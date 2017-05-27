def addOperators(num, target, v = 0, i = 0, expression = "", memo = { }):
    k = (v, i)
    if k in memo:
        print "HIT"
        return memo[k]
    print num, target, v, i, expression
    results = []
    if len(num) == 1:
        if target == int(num):
            return [num]
    if i == len(num) - 1:
        if v + int(num[i]) == target:
            results.append(expression + "+" + num[i])
        if v * int(num[i]) == target:
            results.append(expression + "*" + num[i])
        if v - int(num[i]) == target:
            results.append(expression + "-" + num[i])
        #print results
        return results
    if i == 0:
        results.extend(addOperators(num, target, int(num[i]), i + 1, num[i], memo))
    else:
        results.extend(addOperators(num, target, v + int(num[i]), i + 1, expression + "+" + num[i], memo))
        results.extend(addOperators(num, target, v - int(num[i]), i + 1, expression + "-" + num[i], memo))
        results.extend(addOperators(num, target, v * int(num[i]), i + 1, expression + "*" + num[i], memo))
        memo[k] = results
    return results

print addOperators("105", 5)
