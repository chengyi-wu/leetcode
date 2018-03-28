'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    '''
    https://leetcode.com/problems/implement-trie-prefix-tree/
    '''
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        i = 0
        n = self.root
        while i < len(word):
            c = word[i]
            if c in n.children:
                n = n.children[c]
            else:
                break
            i += 1
        while i < len(word):
            c = word[i]
            n.children[c] = TrieNode()
            n = n.children[c]
            i += 1

        n.end = True
    
    def prefixLookup(self, prefix):
        if len(prefix) == 0:
            return None
        i = 0
        n = self.root
        while i < len(prefix):
            c = prefix[i]
            if c in n.children:
                n = n.children[c]
            else:
                return None
            i += 1
        return n

    def search(self, word):
        n = self.prefixLookup(word)
        if n is None:
            return False
        return n.end

    def startsWith(self, prefix):
        return self.prefixLookup(prefix) is not None

def dfs(board, path, prefix, trie, ret):
    if not trie.startsWith(prefix):
        print("dfs :", prefix)
        return
    if trie.search(prefix) and prefix not in ret:
        ret.append(prefix)
    
    row, col = len(board), len(board[0])
    next_pos = []

    x, y = path[-1]
    if x - 1 >= 0:
        next_pos.append((x - 1, y))
    if x + 1 < row:
        next_pos.append((x + 1, y))
    if y - 1 >= 0:
        next_pos.append((x, y - 1))
    if y + 1 < col:
        next_pos.append((x, y + 1))
    
    for pos in next_pos:
        if pos not in path:    
            x, y = pos
            c = board[x][y]
            dfs(board, path + [pos], prefix + c, trie, ret)

def findWords(board, words):
    tire = Trie()
    for word in words:
        tire.insert(word)

    ret = []

    row, col = len(board), len(board[0])

    for i in range(row):
        for j in range(col):
            dfs(board, [(i, j)], board[i][j], tire, ret)

    return ret
    

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words =  ["oath","pea","eat","rain", "oathf", "oathh"] 

print(findWords(board, words))



        
        