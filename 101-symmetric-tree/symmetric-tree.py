# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # if(root.left.val==root.right.val):
        #     check_if_true(root.left,root.right)


        def check_if_true(l,r):

 
            if not l and not r:
                return True
            if not l or not  r:
                return False
                
            if l.val!= r.val:
                return False
  

            return check_if_true(l.right,r.left) and check_if_true(l.left,r.right)
             
        
            
        return check_if_true(root.left,root.right)
    





            
        return False

        