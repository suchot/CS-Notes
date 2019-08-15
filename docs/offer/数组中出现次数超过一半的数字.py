# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        start, end = 0, len(numbers)-1
        self.quicksort(numbers, start, end)
        majority = numbers[len(numbers)>>1]
        c = 0
        for number in numbers:
            if number == majority:
                c +=1
        if c>(len(numbers)>>1):
            return majority
        else:
            return 0
        return majority
    def quicksort(self, numbers, start, end):
        index = self.partition(numbers, start, end)
        if start < end:
            self.partition(numbers,start, index-1)
            self.partition(numbers,index+1, end)
            
    def partition(self, nums, start, end):
        self.swap(nums,start, end)
        pivot = nums[end]
        small = start-1
        for index in range(start, end):
            if nums[index]<pivot:
                small += 1
                if small < index:
                    self.swap(nums,small, index)
        small += 1
        self.swap(nums, small, end)
        return small
    def swap(self, array, a, b):
        array[a], array[b] = array[b], array[a]
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        majority = numbers[0]
        count = 1
        for number in numbers:
            if count == 0:
                majority = number
                count = 1
            elif number==majority:
                count+= 1
            else:
                count -= 1
        c = 0
        for number in numbers:
            if number == majority:
                c +=1
        if c>(len(numbers)>>1):
            return majority
        else:
            return 0

