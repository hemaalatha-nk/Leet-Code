class Solution:
    def maxArea(self, height: List[int]) -> int:
        r, l=len(height)-1,0
        res=0
        while l<r:
            area=(r-l)* min(height[r], height[l])
            res= max(res,area)
            if(height[l]<=height[r]):
                l+=1
            else:
                r-=1
        return res