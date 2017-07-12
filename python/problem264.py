'''
https://leetcode.com/problems/ugly-number-ii/#/description
https://leetcode.com/submissions/detail/107823491/
'''

def nthUglyNumber(n):
    '''
    type n: int
    rtype: int
    '''
    numbers = [1]
    k = 1
    i2, i3, i5 = 0,0,0
    while k != n:
        un2, un3, un5 = numbers[i2] * 2, numbers[i3] * 3, numbers[i5] * 5
        un = min(un2, un3, un5)
        if un == un2:
            i2 += 1
        if un == un3:
            i3 += 1
        if un == un5:
            i5 += 1
        numbers.append(un)
        k += 1
    return numbers[-1]

def test():
    for i in range(1,20):
        print nthUglyNumber(i)
    print nthUglyNumber(1690)

test()
