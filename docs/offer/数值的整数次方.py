# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        isnegetive = False
        if exponent < 0:
            isnegetive = True
            exponent = abs(exponent)
        else:
            pass
        res = self.Power(base*base, exponent>>1)
        if exponent%2 == 1:
            res = base*res
        if not isnegetive:
            return res
        else:
            return 1/res
