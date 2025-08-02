class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        prev=points[0]
        res=len(points)

        for i in range(1, len(points)):
            cur=points[i]
            if(cur[0]<=prev[1]):
                res-=1
                prev=[cur[0],min(cur[1],prev[1])]
            else:
                prev=cur
        return res

        