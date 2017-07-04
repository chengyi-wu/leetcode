
def solve(board):
    row = len(board)
    if row == 0:
        return
    col = len(board[0])
    c = 0
    matrix = []
    regions = []
    for i in range(row):
        r = []
        for j in range(col):
            r.append(c)
            regions.append([c, i, j])
            c += 1
        matrix.append(r)
    #print matrix
    edges = []
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'O':
                if i - 1 >= 0 and board[i - 1][j] == 'O':
                    #matrix[i][j] = matrix[i - 1][j]
                    #connect (i,j) and (i - 1, j)
                    print "conect", matrix[i - 1][j], matrix[i][j], matrix[i - 1][j]
                    #regions[matrix[i - 1][j]] = matrix[i][j]
                    p = matrix[i - 1][j]
                    for z, region in enumerate(regions):
                        if region[0] == p:
                            regions[z][0] = matrix[i][j]
                if j - 1 >= 0 and board[i][j - 1] == 'O':
                    #matrix[i][j] = matrix[i][j - 1]
                    print "conect", matrix[i][j - 1], matrix[i][j], matrix[i][j - 1]
                    #regions[matrix[i][j] - 1] = matrix[i][j]
                    #connect (i, j) and (i, j - 1)
                    p = matrix[i][j - 1]
                    for z, region in enumerate(regions):
                        if region[0] == p:
                            regions[z][0] = matrix[i][j]
    print regions
    #return
    edges = []
    c = 0
    for i in range(row):
        for j in range(col):
            print regions[c][0],
            if board[i][j] == 'O':
                #regions.append((matrix[i][j], i , j))

                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    edges.append(regions[c][0])
            c += 1
        print
    print edges
    for region in regions:
        if region[0] not in edges:
            #print region, region[0] not in edges
            x = region[1]
            y = region[2]
            #print x, y, board[x][y], matrix[x][y]
            board[x][y] = 'X'
    for r in board:
        print ''.join(r)

def test():
    board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    board = ["OXXOX","XOOXO","XOXOX","OXOOO","XXOXO"]
    board = ["XOOXXXOXOO","XOXXXXXXXX","XXXXOXXXXX","XOXXXOXXXO","OXXXOXOXOX","XXOXXOOXXX","OXXOOXOXXO","OXXXXXOXXX","XOOXXOXXOO","XXXOOXOXXO"]
    board = ["XXXXOOXXO","OOOOXXOOX","XOXOOXXOX","OOXXXOOOO","XOOXXXXXO","OOXOXOXOX","OOOXXOXOX","OOOXOOOXO","OXOOOXOXO"]
    board = ["OOOOXX","OOOOOO","OXOXOO","OXOOXO","OXOXOO","OXOOOO"]
    for i, row in enumerate(board):
        print row
        board[i] = list(row)
    solve(board)

test()
