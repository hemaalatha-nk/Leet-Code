class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]


        prev=nums[0]
        cur=max(nums[0],nums[1])

        for i in range(2,n):
            prev, cur =cur, max(cur, prev+nums[i])
            

        return cur

       


        