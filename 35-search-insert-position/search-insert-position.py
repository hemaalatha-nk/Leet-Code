class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1


        while l<=r :
            m=(l+r)//2 
            
            if target<nums[m]:
                r=m-1
            elif target> nums[m]:
                l=m+1
            else:
                return m
        if nums[m]<target:
            return m+1
        else:
            return m

            # time: O(log(n))








        