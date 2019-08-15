class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        maxlen = 0
        dp = [[0 for i in range(cols+1)] for j in range(rows+1)]
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen**2

if __name__ == "__main__":
    S = Solution()
    matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    S.maximalSquare(matrix)