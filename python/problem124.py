class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

  
def dfs(root):
    



    
    

def maxPathSum(root):
    trail = []
    dfs(root, trail)
    return max(trail)
    


    
    
def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    #root.left.right = TreeNode(2)
    #root.right.left = TreeNode(3)
    print maxPathSum(root)

test()