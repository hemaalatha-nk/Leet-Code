# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res=[]
        queue=[]
        queue.append(root)

        while queue:
            bfs=len(queue)
            leve=[]

            for i in range(0,bfs):
                node=queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                leve.append(node.val)
            
            res.append(leve)
        return res



        

     


        