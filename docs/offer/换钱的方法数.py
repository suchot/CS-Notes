class Solution():
    def changecoin(self, arr, aim):
        if not arr or aim<0:
            return 0
        dp = [[0 for i in range(aim+1)] for j in range(len(arr))]
        for i in range(len(arr)):
            dp[i][0]=1
        j=1
        while arr[0]*j<=aim:
            dp[0][j*arr[0]]=1 # 只用货币0一种时的可以达到的钱的方法数
            j +=1
        for i in range(1, len(arr)):
            for j in range(1, aim+1):
                if j-arr[i]>=0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-arr[i]]
                else:
                    dp[i][j] = dp[i-1][j] 
        return dp[-1][-1]
if __name__ == "__main__":
    S = Solution()
   # n,arr,aim = 4, [5, 10, 25, 1], 15

    n,arr,aim = 5, [2, 3, 5, 7, 10], 1000

    print(S.changecoin(arr, aim))
