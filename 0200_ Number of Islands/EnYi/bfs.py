class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]
        island = [[0 for i in range(col)] for j in range(row)]
        count = 0        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and island[i][j] == 0:
                    temp = deque()
                    temp.append([i, j])
                    island[i][j] = 1                    
                    while temp:
                        trow, tcol = temp.popleft()
                        for dx, dy in direction:
                            x = trow + dx
                            y = tcol + dy  
                            if 0 <= x < row and 0 <= y < col:
                                if grid[x][y] == '1' and island[x][y] == 0:
                                    temp.append([x, y])
                                    island[x][y] = 1
                    count += 1
        return count