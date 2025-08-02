class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=0
        ans=0
        nums=list(sorted(set(nums)))
        if len(nums)==0:
            return 0

        for r in range(1,len(nums)):
            if(nums[r-1]+1==nums[r]):
                ans=max(r-l,ans)
                continue
            else:
                l=r
        return (ans+1)
            
        


            



        