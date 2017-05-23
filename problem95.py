'''
https://leetcode.com/problems/unique-binary-search-trees-ii/#/description

https://leetcode.com/submissions/detail/103740135/
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

def buildTree(inorder):
    #print inorder
    if len(inorder) == 0:
        return [None]
    if len(inorder) == 0:
        return [TreeNode(inorder[0])]
    results = []
    for i in range(len(inorder)):
        left = buildTree(inorder[:i])
        right = buildTree(inorder[i + 1:])
        for l in left:
            for r in right:
                n = TreeNode(inorder[i])
                n.left = l
                n.right = r
                results.append(n)
    return results

def numTrees(n):
    if n == 0:
        return []
    inorder = [str(x) for x in range(1, n + 1)]
    return buildTree(inorder)

def preorderWalk(n):
    if n != None:
        print n,
        preorderWalk(n.left)
        preorderWalk(n.right)

def test_buildTree(inorder):
    for t in buildTree(inorder):
        preorderWalk(t)
        print ""
def test_numTrees(n):
    trees = numTrees(n)
    print("%d different tree(s)."%(len(trees)))
    for t in trees:
        preorderWalk(t)
        print ""

test_buildTree("123")
test_numTrees(3)
test_numTrees(0)
