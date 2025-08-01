class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        
        rowEnd=len(matrix)-1
        colEnd=len(matrix[0])-1

        rowBegin=0
        colBegin=0
        ans=[]

        while( rowBegin<=rowEnd and colBegin<=colEnd):

            # go right
            for i in range(colBegin,colEnd+1):
                # print("i",i)
                print(matrix[rowBegin][i])
                ans.append(matrix[rowBegin][i])
            rowBegin+=1

            # go down
            for j in range(rowBegin,rowEnd+1):
                print(matrix[j][colEnd])
                ans.append(matrix[j][colEnd])
            colEnd-=1

            #go left
            # print(colBegin, colEnd+1)
            if rowBegin<=rowEnd:
                for k in range( colEnd,colBegin-1,-1):
                    # print("k",k)
                    print(matrix[rowEnd][k])
                    ans.append(matrix[rowEnd][k])
                rowEnd-=1

            #go up
            if colBegin<=colEnd:
                for l in range(rowEnd,rowBegin-1,-1):
                    print(matrix[l][colBegin])
                    ans.append(matrix[l][colBegin])
                colBegin+=1
    
        return ans

