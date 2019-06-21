# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        #因为是排序好的序列所以可以用双指针法来得对应位的位置
        p1, p2 = 0, len(array)-1
        while(p1<p2):
            sum = array[p1] +array[p2]
            if sum == tsum:
                return [array[p1], array[p2]]
            if sum > tsum:
                p2 -= 1
            else:
                p1 += 1
        return []