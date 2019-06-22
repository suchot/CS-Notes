# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n==0:
            return -1
        if n==1:
            return 0 
        dp = 0
        for i in range(1,n+1):
            dp = (dp+m)%i
        return dp
