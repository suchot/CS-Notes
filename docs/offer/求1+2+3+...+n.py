# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n > 0 and (n+self.Sum_Solution(n-1))

