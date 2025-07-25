# Last updated: 7/24/2025, 1:40:58 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.pop(0)#root
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth +=1 #updating depth

        return depth


            



        