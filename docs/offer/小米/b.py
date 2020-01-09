class Solution(object):
    def profit(self, prices):
        if not prices:
             return 0
        n = len(prices)
        dp = [[0 for i in range(n)] for j in range(3)]
        for k in range(1, 3):
            pre_max = -prices[0]
            for i in range(1, n):
                pre_max = max(pre_max, dp[k - 1][i - 1] - prices[i])
                dp[k][i] = max(dp[k][i - 1], prices[i] + pre_max)
        return dp[-1][-1]


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    S = Solution()
    print(S.profit(arr))