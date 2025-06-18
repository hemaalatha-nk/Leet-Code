class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
          return s
        res=[[] for _ in range(numRows)]
        j=0
        downwards=1

        for i in range(len(s)):
            res[j].append(s[i])
            if(j==(numRows-1)):
                downwards=-1
            if(j==0):
                downwards=1
            j=j+downwards

        return ''.join(char for sublist in res for char in sublist)
        