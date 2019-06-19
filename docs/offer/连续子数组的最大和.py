# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        dp = array
        for i in range(1, len(array)):
            if i==0 or dp[i-1]<=0:
                dp[i] = array[i]
            elif dp[i-1]>0:
                dp[i] = dp[i-1] + array[i]
        return max(dp)
        
