# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        C = [1 for i in range(length)]
        if length <=1:
            return A
        for i in range(1, length):
            C[i] = C[i-1] * A[i-1]
        temp = 1
        for i in range(length-2, -1, -1):
            temp *= A[i+1]
            C[i] *= temp 
        return C
            
