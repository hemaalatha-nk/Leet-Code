class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res=[[] for _ in range(numRows)]
        print(res)
        j=0
        downwards=True
        if(numRows==1):
            return s
        for i in range(len(s)):
            
            print(j, downwards, s[i])
            res[j].append(s[i])
            
            if(j==(numRows-1)):
                downwards=False
                print(res)
            if(j==0):
                # print(j, downwards)
                downwards=True
        
            if(downwards):
                j=j+1
            else:
                j=j-1
        return ''.join(char for sublist in res for char in sublist)
        