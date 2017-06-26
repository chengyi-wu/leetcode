class TreeNode(object):
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)

    def find(self, k):
        #print self, k
        if self.key == k:
            return self
        if self.left != None and self.key > k:
            return self.left.find(k)
        if self.right != None and self.key < k:
            return self.right.find(k)
        return None

    def find_min(self):
        if self.left == None:
            return self
        return self.left.find_min()

    def find_max(self):
        if self.right == None:
            return self
        return self.right.find_max()

    def next_larger(self):
        if self.right != None:
            return self.right.find_min()
        parent = self.parent
        n = self
        while parent != None and n != parent.left:
            n = parent
            parent = parent.parent
        return parent

    def next_smaller(self):
        if self.left != None:
            return self.left.find_max()
        parent = self.parent
        n = self
        while parent != None and n != parent.right:
            n = parent
            parent = parent.parent
        return parent

    def insert(self, node):
        if self.key < node.key:
            if self.right != None:
                self.right.insert(node)
            else:
                self.right = node
                node.parent = self
        elif self.key > node.key:
            if self.left != None:
                self.left.insert(node)
            else:
                self.left = node
                node.parent = self
        else:
            raise RuntimeError("EQUAL is NOT ALLOWED FOR NOW")

    def delete(self):
        '''
        3 cases:
        1. node has 0 child: update the parent's left or right to None
        2. node has 1 child
        3. node has 2 children
        '''
        #print "delete()", self
        if self.left == None and self.right == None:
            if self.parent != None:
                if self == self.parent.left:
                    self.parent.left = None
                else:
                    self.parent.right = None
        elif self.left == None or self.right == None:
            if self.left == None:
                n = self.right
            else:
                n = self.left
            if self.parent != None:
                if self.parent.left == self:
                    self.parent.left = n
                else:
                    self.parent.right = n
                    n.parent = self.parent
        #elif self.left != None and self.right != None:
        else:
            #remove the successor from the subtree
            succ = self.next_larger()
            succ.delete()
            #print "remove the successor:", succ
            if self.parent != None:
                if self == self.parent.left:
                    self.parent.left = succ
                else:
                    self.parent.right = succ
            succ.parent = self.parent
            succ.left = self.left
            succ.right = self.right
            #print "put it under", self.parent
        return self

class BST(object):
    def __init__(self):
        self.root = None
    def insert(self, k):
        n = TreeNode(k)
        if self.root == None:
            self.root = n
        else:
            self.root.insert(n)

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print node,
        self.inorder(node.right)

    def find(self, k):
        if self.root == None:
            return None
        return self.root.find(k)

    def delete(self, k):
        n = self.find(k)
        if n == None:
            raise None
        if n == self.root:
            self.root = n.next_larger()
            if self.root == None:
                self.root = n.next_smaller()
        return n.delete()

def test():
    items = [1,2,3,4,5,6,7,8,9]
    tree = BST()
    for n in items:
        tree.insert(n)
    tree.inorder(tree.root)
    print
    #print tree.root.left.next_larger()
    #print tree.root.left.next_smaller()
    print tree.delete(7)
    print tree.delete(6)
    print tree.delete(1)
    tree.inorder(tree.root)
    print

test()
