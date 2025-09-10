class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
 

        def binsearch(leftBias):

            l=0
            r=len(nums)-1
            i=-1
            while l<=r:
                m=(l+r)//2

                if nums[m]<target:
                    l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    i=m
                    if leftBias:
                        r=m-1
                    else:
                        l=m+1
            return i

        return[binsearch(True),binsearch(False)]

        