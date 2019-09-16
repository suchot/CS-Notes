class MinCost:
    def findMinCost(self, A, n, B, m, c0, c1, c2):
        dp=[[0 for i in range(m+1)]for i in range(n+1)]
        for i in range(n+1):#初始化dp[0][j]
            dp[i][0]=i*c1
        for j in range(m+1):#初始化dp[i][0]
            dp[0][j]=j*c0
        for i in range(1,n+1):#其他情况
            for j in range(1,m+1):
                dp[i][j]=min(dp[i-1][j]+c1,dp[i][j-1]+c0)
                if A[i-1]==B[j-1]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j])
                else:
                    dp[i][j]=min(dp[i-1][j-1]+c2,dp[i][j])
        return dp[n][m]
