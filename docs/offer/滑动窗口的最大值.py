# -*- coding:utf-8 -*-
import collections 
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        deques = collections.deque()
        res =[]
        if len(num) <size or size < 1:
            return []
        start, end = 0, len(num)
        while start < end:
            if deques and start - deques[0] >= size:
                deques.popleft()
            while deques and num[deques[-1]] < num[start]:
                    deques.pop()
            deques.append(start)
            if start >= size -1:
                res.append(num[deques[0]])
            start += 1
        return res
        