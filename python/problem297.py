'''
The serialization of general binary tree can be done by using PREORDER and INORDER of the BST
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Codec:

    def InorderWalk(self, root):
        if root != None:
            self.InorderWalk(root.left)
            self.inorder.append(self.encode(root))
            self.InorderWalk(root.right)
    def PreorderWalk(self, root):
        if root != None:
            self.preorder.append(self.encode(root))
            self.PreorderWalk(root.left)
            self.PreorderWalk(root.right)
    def serialize(self, root):
        self.inorder = []
        self.preorder = []
        self.InorderWalk(root)
        self.PreorderWalk(root)
        #print self.inorder
        #print self.preorder
        if len(self.inorder) == 0:
            return ""
        return ','.join(self.inorder) + "#" + ','.join(self.preorder)
    def deserialize(self, data):
        if len(data) == 0:
            return None
        inorder = data.split("#")[0].split(',')
        preorder = data.split("#")[1].split(',')
        #print inorder
        #print preorder
        return self.buildTree(preorder, inorder)
    def encode(self, root):
        return str(id(root)) + '*' + str(root.val)
    def decode(self, s):
        return int(s.split('*')[1])
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(self.decode(preorder[0]))
        i = inorder.index(preorder[0])
        leftInorder = inorder[:i]
        rightInorder = inorder[i + 1:]

        i = 1 + len(leftInorder)
        leftPreorder = preorder[1:i]
        rightPreorder = preorder[i:]

        n = TreeNode(self.decode(preorder[0]))
        n.left = self.buildTree(leftPreorder, leftInorder)
        n.right = self.buildTree(rightPreorder, rightInorder)

        return n

def test():
    codec = Codec()
    n = TreeNode(10)
    n.left = TreeNode(5)
    n.left.left = TreeNode(2)
    n.left.right = TreeNode(7)
    n.right = TreeNode(15)
    #ser = "9,7,5,3,1,2,4,6,8,10,12,14,16,18,19,17,15,13,11,1#1,10,9,8,7,6,5,4,3,2,1,11,12,13,14,15,16,17,18,19"
    ser = codec.serialize(n)
    print ser
    n = codec.deserialize(ser)
    print n, n.left, n.right, n.left.left, n.left.right

test()
