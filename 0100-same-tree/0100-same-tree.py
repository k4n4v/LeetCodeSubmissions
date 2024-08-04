# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: # if p and q are empty
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        # both trees not empty and values are the same
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        
        
            