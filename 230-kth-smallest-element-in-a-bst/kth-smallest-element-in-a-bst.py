# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=[k]
        ans=[0]

        def find_smallest(node):
            if not node:
                return 

            find_smallest(node.left )

            if count[0]==1:
                ans[0]=node.val
            
            count[0]=count[0]-1
            if count[0] >0:
                find_smallest(node.right)
        find_smallest(root)
        return ans[0]
            

            

        