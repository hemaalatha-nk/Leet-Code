class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(0,9):
            row=set()
            for c in range(0,9):
                if(board[r][c] in row):
                    return False
                elif(board[r][c]=="."):
                    continue
                else:
                    row.add(board[r][c])
            
        for c in range(0,9):
            col=set()
            for r in range(0,9):
                if(board[r][c] in col):
                    return False
                elif(board[r][c]=="."):
                    continue
                else:
                    col.add(board[r][c])


        grid=[(0,0),(0,3),(0,6),
                (3,0),(3,3),(3,6),
                (6,0),(6,3),(6,6)]
    
        for i,j in grid:
            box=set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    if(board[r][c] in box):
                        return False
                    elif(board[r][c]!="."):
                        box.add(board[r][c])
        return True



        