# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        for i in range(len(numbers)-1):
            for j in range(len(numbers)-1-i):
                if self.compare(numbers[j],numbers[j+1]):
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        res = ''.join(list(map(str, numbers))).lstrip('0')
        return res or '0'
　   # 这道题主要是定义一个比较函数
    def compare(self, str1, str2):
        s1 = str(str1) +str(str2)
        s2 = str(str2) + str(str1)
        if s1 > s2:
            return True
        else:
            return False
