from collections import deque
 
class Solution:
    def __init__(self):
        self.count = 0
    def InversePairs(self, lis):
        # write code here
        self.mergeSort(lis)
        return self.count%1000000007

    def mergeSort(self, lis):
        if len(lis) <= 1:
            return lis
        middle = int(len(lis)//2)
        left = self.mergeSort(lis[:middle])
        right = self.mergeSort(lis[middle:])
        return self.merge(left, right)
    def merge(self, left,right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            if left[0] > right[0]:
                self.count += len(left)
                merged.append(right.popleft())
            else:
                merged.append(left.popleft())
        if right:
            merged.extend(right)
        else:
            merged.extend(left)
        return merged