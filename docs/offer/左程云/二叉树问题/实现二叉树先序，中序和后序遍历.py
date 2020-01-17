# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None, right=None):
        if left==0:
            left=None
        if right==0:
            right=None
        self.val = x
        self.left = left
        self.right = right
if __name__ == "__main__":
    n, root = map(int, input().split())
    root =TreeNode(root)
    for i in range(n):
            a,b,c = map(int, input().split())
            TreeNode(a,b,c)
    pass

# def input2binarytree(self,root, left_leaf, right_leaf):
#     return 
