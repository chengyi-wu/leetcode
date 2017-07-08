def kthSmallest(matrix, k):
    '''
    Convert the matrix to 1D array, sort the array and return the value
    '''
    row = len(matrix)
    col = len(matrix[0])
    #list comprehension is much faster
    nums = [matrix[i][j] for i in range(row) for j in range(col)]
    nums.sort()
    
    return nums[k - 1]