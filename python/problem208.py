'''
Tries, a.k.a. RADIX Tree
'''

class TrieNode(object):
    def __init__(self, x = None):
        self.children = { }
        self.endofWord = False
        if x != None:
            self.children[x] = TrieNode()
    def SetEndofWord(self, endofWord):
        self.endofWord = endofWord
    def IsEndofWord(self):
        return self.endofWord
    #def __str__(self):
        #return str(self.key)

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.root.SetEndofWord(True)

    def insert(self, word):
        n = self.root
        for i, w in enumerate(word):
            if w not in n.children:
                n.children[w] = TrieNode()
            if i == len(word) - 1:
                n.children[w].SetEndofWord(True)
            n = n.children[w]
        self.debugCheck(self.root)

    def search(self, word):
        n = self.root
        for i, w in enumerate(word):
            if w not in n.children:
                return False
            n = n.children[w]
        return n.IsEndofWord()
    def startsWith(self, prefix):
        n = self.root
        for i, w in enumerate(prefix):
            if w not in n.children:
                return False
            n = n.children[w]
        return True
    def debugCheck(self, n):
        print n.children.keys()
        for c in n.children:
            self.debugCheck(n.children[c])

def test_Trie():
    tree = Trie()
    tree.insert("a")
    #tree.insert("abcd")
    print tree.search("a")
    print tree.startsWith("a")

test_Trie()
