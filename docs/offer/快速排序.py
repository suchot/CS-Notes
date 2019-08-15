# -*- coding:utf-8 -*-
class Solution:
    def quicksort(self, array):
        start, end  = 0, len(array)-1
        if end <= 0:
            return array 
        return self.quicksortCore(array, start, end)
    def quicksortCore(self, array, start, end):
        index = self.partition(array, start, end)
        if start<end:
            self.quicksortCore(array, start, index-1)
            self.quicksortCore(array, index+1, end)
        return array
    def partition(self, array, start, end):
        self.swap(array, start, end)
        small = start - 1 
        for index in range(start, end):
            if array[index] < array[end]:
                small += 1
                if small != index:
                    self.swap(array, index, small)
        small += 1
        self.swap(array, small, end)
        return small 
    def swap(self, array, a, b):
        array[a], array[b] = array[b], array[a]
if __name__ == "__main__":
    array = [4,1,2,3,5,6,7,1,4,64,2,23]
    S = Solution()
    print(S.quicksort(array))
        