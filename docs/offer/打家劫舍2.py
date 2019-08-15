class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        return max(self.robcore(nums[0:-1]), self.robcore(nums[1::]))
    
    def robcore(self, nums):
        dp = [0]*len(nums)       
        for i in range(len(nums)):
            if i==0:
                dp[i]=nums[0]
                continue
            dp[i]= max(dp[i-1], dp[i-2]+nums[i])
        
        return dp[-1]
if __name__ == "__main__":
    nums = [1,2,3,1]
    S = Solution()
    print(S.rob(nums))