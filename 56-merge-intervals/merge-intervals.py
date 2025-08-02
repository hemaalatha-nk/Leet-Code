class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda interval: interval[0])

        ans=[]
        start=intervals[0][0]
        end=intervals[0][1]

        for i in intervals:

            if not ans or ans[-1][1]<i[0]:
                ans.append(i)
            else:
                ans[-1]=[ans[-1][0],max(i[1],ans[-1][1])]
        return(ans)
          