# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root1, root2):
        if root1 and not root2 or not root1 and root2:
            return False
        if not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.helper(root, root)
    Comments: 1
    
    
    