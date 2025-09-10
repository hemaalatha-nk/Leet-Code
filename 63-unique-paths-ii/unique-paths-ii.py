class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid),len(obstacleGrid[0])
        @cache
        def dp(r,c):
            if r==m or c==n or obstacleGrid[r][c]==1:
                return 0
            if (r,c)==(m-1,n-1):
                return 1
            
            return dp(r+1,c)+dp(r,c+1)

        
        return dp(0,0)
        