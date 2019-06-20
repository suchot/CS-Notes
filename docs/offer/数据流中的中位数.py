# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def Insert(self, num):
        # write code here
        self.arr.append(num)
        self.arr.sort()
    def GetMedian(self,mid=None):
        # write code here
        lens = len(self.arr)
        if lens&1 == 1:
            mid = lens>>1
            return self.arr[mid]
        elif lens == 0:
                return []
        else:
            return (self.arr[lens>>1]+self.arr[(lens>>1) -1])/2.0
            
