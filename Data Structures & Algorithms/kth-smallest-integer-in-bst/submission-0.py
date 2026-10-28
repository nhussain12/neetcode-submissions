# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inOrderTraversal(node) -> List[int]:
            if node:
                inOrderTraversal(node.left)

                res.append(node.val)

                inOrderTraversal(node.right)

            return res

        sorted_values = inOrderTraversal(root)
        
        return sorted_values[k - 1]

