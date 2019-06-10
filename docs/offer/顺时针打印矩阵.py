# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        r1 = 0
        r2 = len(matrix) - 1
        c1 = 0
        c2 = len(matrix[0]) - 1
        if  r2 < 0 or c2 < 0:
            return res
        while r1<=r2 and c1<=c2:
            for i in range(c1, c2+1):
                res.append(matrix[r1][i])
            for i in range(r1+1, r2+1):
                res.append(matrix[i][c2])
            if (r1 != r2):
                for i in range(c2-1, c1-1, -1):
                    res.append(matrix[r2][i])
            if c1 != c2:
                for i in range(r2-1, r1, -1):
                    res.append(matrix[i][c1])

            r1 += 1 
            r2 -= 1
            c1 += 1 
            c2 -= 1
        return res