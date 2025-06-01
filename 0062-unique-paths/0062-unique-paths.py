class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        dp = [1] * n  # Initialize first row with 1s
        for i in range(1, m):
            new_row = [1]  # First column has 1 way
            for j in range(1, n):
                new_row.append(dp[j] + new_row[j-1])
            dp = new_row
        return dp[n-1]