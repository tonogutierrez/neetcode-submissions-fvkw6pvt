class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #Add fresh oranges to know how many they are
                if grid[i][j] == 1:
                    fresh += 1
                #Append the rotten fruits
                #We need to know vertically adjacent to a rotten fruit
                if grid[i][j] == 2:
                    q.append((i,j))
            
            #DPS
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, dc + c
                    if(nr in range(len(grid)) and
                        nc in range(len(grid[0]))and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1



        
                
