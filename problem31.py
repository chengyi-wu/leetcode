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
    #nums[j], nums[i] = nums[i], nums[j]
    t = nums[i]
    nums[i] = nums[j]
    nums[j] = t
    #print "swap",i,j

def nextPermutation(nums):
    '''
    1. Scan the sequence from right to left, find the first non-incresing poisition, front.
    2. Scan the sequence again from right to left, find the first element which is lexically larger than S[front], rear
    3. Swap the front and rear
    4. Increment front by one and set the rear to the end
    5. Swap front and rear respectively till they meet
    '''
    front = -1
    for i in reversed(xrange(1, len(nums))):
        if nums[i] > nums[i - 1]:
            front = i - 1
            break
    if front > -1:
        rear = len(nums) - 1
        #while nums[front] >= nums[rear]:
        #    rear -= 1
        #using a for loop instead of while loop
        for i in reversed(xrange(front + 1, len(nums))):
            if nums[front] < nums[i]:
                rear = i
                break
        swap(nums, front, rear)
    front += 1
    rear = len(nums) - 1
    while front < rear:
        swap(nums, front, rear)
        front += 1
        rear -= 1
    return ''.join(nums)

if __name__ == '__main__':
    #print permutation("XYZ")
    #print nextPermutation(list('BCA'))
    print nextPermutation(list('151'))
    #print nextPermutation(list('321'))
    s = "ABCDE"
    nums = list(s)
    t = ""
    while s != t:
        t = nextPermutation(nums)
        print t
        
