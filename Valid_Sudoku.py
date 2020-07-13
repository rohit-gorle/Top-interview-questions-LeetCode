class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(0,9):
            for j in range(0,9):
                n = board[i][j]
                if n != '.':
                    if (n,i) in seen or (j,n) in seen or (i//3,j//3,n) in seen:
                        return 0
                    seen.add((n,i))
                    seen.add((j,n))
                    seen.add((i//3,j//3,n))
        return 1 
