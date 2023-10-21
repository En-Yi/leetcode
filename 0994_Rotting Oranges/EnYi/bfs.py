class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min_minutes = 0
        row = len(grid)
        col = len(grid[0])
        rotten_loc_f = deque() # distinguished to count minutes
        rotten_loc = deque() # to replace f
        fresh = [] # record 1 location
        direction = [[1,0],[0,1],[-1,0],[0,-1]]        

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:                    
                    rotten_loc_f.append([i,j])
                if grid[i][j] == 1:
                    fresh.append([i,j])
        
        while len(fresh) > 0:                
            while len(rotten_loc_f) > 0:
                r, c = rotten_loc_f.popleft()
                if (r+1 <= row-1):
                    if grid[r+1][c] == 1:
                        grid[r+1][c] = 2
                        rotten_loc.append([r+1,c])
                        fresh.remove([r+1,c])
                if (0 <= r-1):
                    if grid[r-1][c] == 1:
                        grid[r-1][c] = 2
                        rotten_loc.append([r-1,c])
                        fresh.remove([r-1,c])
                if (c+1 <= col-1):
                    if grid[r][c+1] == 1:
                        grid[r][c+1] = 2
                        rotten_loc.append([r,c+1])
                        fresh.remove([r,c+1])
                if (0 <= c-1):
                    if grid[r][c-1] == 1:
                        grid[r][c-1] = 2
                        rotten_loc.append([r,c-1])
                        fresh.remove([r,c-1])
            if len(rotten_loc) == 0 and len(fresh) > 0:                
                return -1
            if len(rotten_loc) == 0 and len(fresh) == 0:
                return min_minutes
            else:
                min_minutes += 1
                rotten_loc_f, rotten_loc = rotten_loc, rotten_loc_f
        return min_minutes