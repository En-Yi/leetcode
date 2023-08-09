class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 0 or n == 1):
            return 1
        
        # matrix multiplication
        F = [[1, 1],
            [1, 0]]
        A = [1, 1] # f(0) and f(1)
        
        for i in range(n-1):
            x = (F[0][0] * A[0] + F[0][1] * A[1])
            y = (F[1][0] * A[0] + F[1][1] * A[1])
            A[0] = x
            A[1] = y           
    
        return A[0]