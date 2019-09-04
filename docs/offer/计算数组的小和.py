from collections import deque
 
class Solution:
    def __init__(self):
        self.count = 0
    def InversePairs(self, lis):
        # write code here
        self.mergeSort(lis)
        return self.count

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
            if left[0] <= right[0]:
                self.count += left[0]*len(right)
                merged.append(left.popleft())
            else:
                merged.append(right.popleft())
        if right:
            merged.extend(right)
        else:
            merged.extend(left)
        return merged

if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().split()))
    S =Solution()
    print(S.InversePairs(lis))    