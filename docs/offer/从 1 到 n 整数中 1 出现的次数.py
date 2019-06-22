# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res, m = 0, 1
        while n>=m:
            res += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n%m + 1)
            m *= 10
        return res
