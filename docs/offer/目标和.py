class Solution:
    def findTargetSumWays(self, nums, S):
        n_sum = sum(nums)
        if n_sum < S or (S+n_sum)%2 != 0:
            return 0
        w = (S + n_sum)//2
        n = len(nums)
        dp = [0 for i in range(w+1)]
        dp[0] = 1
        for num in nums:
            for i in range(w, num-1, -1):
                dp[i] = dp[i] + dp[i-num]
        return dp[w]

if __name__ =='__main__':
    nums = [3,3,3,4,5]
    Su = 8
    S = Solution()
    print(S.findTargetSumWays(nums, Su))

