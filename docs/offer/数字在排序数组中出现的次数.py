# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        num = 0
        if data:
            first =self.GetFirst(data, k)
            last = self.GetLast(data,k)
            if first > -1 and last> -1:
                num = last- first +1
        return num
    def GetFirst(self, data, k):
        start, end  = 0, len(data)-1
        while start <= end:
            mid = start + ((end-start)>>1)
            if data[mid] >= k:
                end = mid - 1
            if data[mid] < k:
                start = mid + 1
        return start
    def GetLast(self, data, k):
        start, end  = 0, len(data)-1
        while start <= end:
            mid = start + ((end-start)>>1)
            if data[mid] > k:
                end = mid - 1
            if data[mid] <= k:
                start = mid + 1
        return end