# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        majority = numbers[0]
        count = 1
        for i in range(1, len(numbers)):
            if count == 0:
                majority = numbers[i]
                count = 1
            elif majority == numbers[i]:
                count += 1
            else:
                count -= 1
# 最后还需要再判断下是否超过数字长度的一半。不存在的情况下，输出０
        cnt = 0
        for i in numbers:
            if i == majority:
                cnt += 1
            if cnt > len(numbers)/2:
                return majority
        return 0
