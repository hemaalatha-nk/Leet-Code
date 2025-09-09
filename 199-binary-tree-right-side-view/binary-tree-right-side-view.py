# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue=[]
        res=[]
        queue.append(root)
        print(queue)

        while queue:
            bfs=len(queue)
            print(bfs)
            lastval=0

            for i in range(0,bfs):
                node=queue.pop(0)
                lastval=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                print(queue)
            
            res.append(node.val)
        return res




        