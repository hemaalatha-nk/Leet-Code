class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        flag=len(nums)-1
        i=flag-1

        while i>=0:
            if(nums[i]+i>=flag):
                flag=i
            
            i-=1
        
        if(flag==0):
            return True
        else:
            return False
    

        

        