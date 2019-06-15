# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n &= (1<<32)-1
        while n > 0:
            n &=(n-1)
            count += 1
        return count
