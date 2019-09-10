# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.verify(sequence, 0, len(sequence)-1)
    def verify(self, sequence, start, end):
        if end-start < 1: #为什么等于1就不行 小于等于1就可以
            return True
        root_val = sequence[end]
        cutindex = start
        while (cutindex < end and sequence[cutindex] < root_val):
            cutindex += 1
        for i in range(cutindex, end):
            if sequence[i] < root_val:
                return False
        return self.verify(sequence, start, cutindex-1) and \
    self.verify(sequence, cutindex, end - 1)
            
