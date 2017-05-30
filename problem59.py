def fillRow(matrix, seed, i, colStart, colEnd):
    offset = 1
    if colStart > colEnd:
        offset = -1
    for j in range(colStart, colEnd + offset, offset):
        matrix[i][j] = seed
        seed += 1
    return seed

def fillCol(matrix, seed, j, colStart, colEnd):
    offset = 1
    if colStart > colEnd:
        offset = -1
    for i in range(colStart, colEnd + offset, offset):
        matrix[i][j] = seed
        seed += 1
    return seed

def generateMatrix(n):
    rowStart = 0
    rowEnd = n - 1
    colStart = 0
    colEnd = n - 1
    seed = 1
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    while rowStart < rowEnd and colStart < colEnd:
        seed = fillRow(matrix, seed, rowStart, colStart, colEnd)
        rowStart += 1
        seed = fillCol(matrix, seed, colEnd, rowStart, rowEnd)
        colEnd -= 1
        seed = fillRow(matrix, seed, rowEnd, colEnd, colStart)
        rowEnd -= 1
        if n % 2 == 0 and rowEnd + 1 == rowStart:
            continue
        seed = fillCol(matrix, seed, colStart, rowEnd, rowStart)
        colStart += 1
    if n % 2 == 1:
        matrix[rowStart][colStart] = seed
    return matrix

def test_generateMatrix(n):
    matrix = generateMatrix(n)
    for i in range(n):
        print matrix[i]
    print "#####################"

test_generateMatrix(0)
test_generateMatrix(1)
test_generateMatrix(2)
test_generateMatrix(3)
test_generateMatrix(4)
test_generateMatrix(5)
