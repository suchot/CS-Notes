# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small, big = 1, 2
        sum_list = 3
        res = []
        while small < (tsum/2+1):
            if tsum == sum_list:
                res.append([i for i in range(small, big+1)])
                big += 1
                sum_list += big
            elif  sum_list> tsum:
                sum_list -= small
                small += 1
            else:
                big += 1
                sum_list += big
        return res 

            