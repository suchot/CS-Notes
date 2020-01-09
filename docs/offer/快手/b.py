class MinCost:
    def findMinCost(self, A, B):
        n = len(A)
        m = len(B)
        dp=[[0 for i in range(m+1)]for i in range(n+1)]
        for i in range(n+1):#初始化dp[0][j]
            dp[i][0]=i
        for j in range(m+1):#初始化dp[i][0]
            dp[0][j]=j
        for i in range(1,n+1):#其他情况
            for j in range(1,m+1):
                dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1)
                if A[i-1]==B[j-1]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j])
                else:
                    dp[i][j]=min(dp[i-1][j-1]+1,dp[i][j])
        return dp[n][m]
if __name__ == "__main__":
    S = MinCost()
    s1 = list(input())
    s2 = list(input())
    print(S.findMinCost(s1,s2))
    