# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        cols, rows = len(array[0]), len(array)
        row, col = 0, cols-1
        while True:
            if col <0 or row >= rows:
                return False
                break
            if array[row][col]==target:
                return True
            elif array[row][col]>target:
                col -= 1
            else:
                row += 1
        return False