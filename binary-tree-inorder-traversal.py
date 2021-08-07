# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    ans = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.ans 
    
    def traverse(self, root):
        if root is None:
            return 
        self.traverse(root.left)
        self.ans.append(root.val)
        self.traverse(root.right)
        
        