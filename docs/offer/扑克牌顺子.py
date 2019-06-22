# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        #
        if len(numbers) != 5:
            return False
        numbers.sort()
        count_zero = 0
        for i in range(len(numbers)-1):
            if numbers[i] == 0:
                count_zero += 1
            elif numbers[i] == numbers[i+1]:
                return False
                 
        max = numbers[-1]
        min = numbers[count_zero]
        if max-min <5:
            return True
        else:
            return False
