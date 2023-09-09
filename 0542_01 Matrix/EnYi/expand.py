class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        queue = deque() # 建立雙向queue，可以雙向操作
        MAX_VALUE = m * n
        
        # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j)) # 收集0的位置
                else:
                    mat[i][j] = MAX_VALUE # 其他位置則設為最大值
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            row, col = queue.popleft() # 取出最左邊的元素
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    queue.append((r, c)) # 加入應改但沒被更改過的位置
                    mat[r][c] = mat[row][col] + 1 # 該位置的距離數值 + 1
        
        return mat