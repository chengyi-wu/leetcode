def kthSmallest(matrix, k):
    '''
    Convert the matrix to 1D array, sort the array and return the value
    '''
    row = len(matrix)
    col = len(matrix[0])
    nums = []
    for i in range(row):
        for j in range(col):
            nums.append((matrix[i][j], i * col + j ))
    nums.sort(key=lambda x:x[0])
    
    n = nums[k - 1][1]
    y = n % col
    x = (n - y) // col
    return matrix[x][y]