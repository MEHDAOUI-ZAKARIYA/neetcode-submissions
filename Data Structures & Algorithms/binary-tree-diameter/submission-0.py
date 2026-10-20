# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diametre = 0

        def dfs (node) :
            nonlocal diametre

            if node is None :
                return 0
            
            leftHeigth = dfs(node.left)
            rigthHigth = dfs(node.right)

            diametre = max(diametre , leftHeigth + rigthHigth)
            return 1 + max(leftHeigth , rigthHigth)

        dfs(root)
        return diametre
        
