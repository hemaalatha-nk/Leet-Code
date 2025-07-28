class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if(sum(nums)<target):
            return 0
        l,sums=0,0
        ans=float("inf")
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                    ans=min(r-l+1, ans)
                    sums-=nums[l]
                    l+=1
            r+=1
        return ans
                    

        