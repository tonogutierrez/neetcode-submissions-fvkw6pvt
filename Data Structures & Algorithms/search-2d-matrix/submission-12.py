class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bot = ROWS - 1

        while top <= bot:
            m = (top + bot) // 2
            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break
        
        #Que pasa si el top y el bot termina la condicion de while
        #Comprobar eso
        # 3 < 2
        if not (top <= bot):
            return False
        
        l = 0
        r = COLS - 1
        row = (top + bot) // 2

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False 