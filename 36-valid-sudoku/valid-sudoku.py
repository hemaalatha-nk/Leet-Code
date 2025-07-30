class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(0,9):
            row=set()
            for c in range(0,9):
                item=board[r][c]
                if(item in row):
                    return False
                elif(item=="."):
                    continue
                else:
                    row.add(item)
            
        for c in range(0,9):
            col=set()
            for r in range(0,9):
                item=board[r][c]
                if(item in col):
                    return False
                elif(item=="."):
                    continue
                else:
                    col.add(item)


        grid=[(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]
    
        for i,j in grid:
            box=set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    item=board[r][c] 
                    if(item in box):
                        return False
                    elif(item!="."):
                        box.add(item)
        return True



        