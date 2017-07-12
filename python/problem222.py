class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

def countNodes(root):
    '''
    Avoid compute a complete subtree
    '''
    #print root
    if root is None:
        return 0
    left = root.left
    right = root.right
    lh = -1
    rh = -1
    while left is not None:
        left = left.left
        lh += 1
    while right is not None:
        right = right.right
        rh += 1
    #print lh, rh
    if lh == -1:
        return 1
    if rh == -1:
        return 2
    if rh == lh:
        #print "rh == lh", 2 **(rh + 2) - 1
        return 2 ** (rh + 2) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)

def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left = TreeNode(7)
    print countNodes(root)

test()
