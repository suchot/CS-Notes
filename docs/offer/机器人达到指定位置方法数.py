class Solution():
    def findways(self,n,m,k,p):
        if n<2 or k<1 or m<1 or m>n or p<1 or p>n:
            return 0
        dp = [[0 for i in range(n+1)] for j in range(k+1)]
        dp[0][p]=1
        for i in range(1, k+1):
            for j in range(1, n+1):
                if j==1:
                    dp[i][j] = dp[i-1][2]
                elif j==n:
                    dp[i][j]=dp[i-1][n-1]
                else:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
        return dp[-1][m]
if __name__ == "__main__":
    S = Solution()
    N,M,K,P = map(int, input().split())
    res = S.findways(N,M,K,P)
    
    print(res%(10**9+7))
