# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            sum12 = num1^num2
            carry = (num1&num2) <<1
            num1 = sum12&((1 << 32)-1)
            num2 = carry&((1 << 32)-1)
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)
