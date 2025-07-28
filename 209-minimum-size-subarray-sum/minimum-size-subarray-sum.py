class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if(sum(nums)<target):
            return 0
        l=0
        r=0
        sums=0
        ans=float("inf")
        while r< len(nums):
            sums+=nums[r]
            print(sums)
            if(sums>=target ):
                # ans=r-l+1
                while sums>=target:
                    ans=min(r-l+1, ans)
                    sums-=nums[l]
                    l+=1
                    print("inside",sums)
            r+=1
        return ans
                    

        