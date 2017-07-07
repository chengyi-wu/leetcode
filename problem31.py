def helper(path, nums):
    if len(nums) == 0:
        return [''.join(path)]
    results = []
    for i, n in enumerate(nums):
        results.extend(helper(path + [n], nums[:i] + nums[i + 1:]))
    return results

def permutation(nums):
    '''
    Naiive algorithm, recursion.
    '''
    return helper([], nums)

def swap(nums, i, j):
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t
    print "swap",i,j

def nextPermutation(nums):
    front = -1
    for i in reversed(range(1, len(nums))):
        if nums[i] > nums[i - 1]:
            front = i - 1
            break
    rear = len(nums) - 1
    while nums[front] > nums[rear]:
        rear -= 1
    if front > -1:
        swap(nums, front, rear)
    front += 1
    while front < rear:
        swap(nums, front, rear)
        front += 1
        rear -= 1
    return ''.join(nums)

if __name__ == '__main__':
    print permutation("XYZ")
    print nextPermutation(list('BCA'))
    #print nextPermutation(list('1234'))
    #print nextPermutation(list('321'))
    #nums = list("ABC")
    #s = ''.join(nums)
    #v = ''
    #while s != v:
    #    v = nextPermutation(nums)
    #    print v
    