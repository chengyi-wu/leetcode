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
    for i in reversed(range(1, len(nums))):
        if nums[i] > nums[i - 1]:
            front = i - 1
            break
    print front 
    if front > -1:
        rear = len(nums) - 1
        while nums[front] >= nums[rear]:
            rear -= 1
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
    