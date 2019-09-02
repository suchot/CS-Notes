import heapq
t, k = map(int, input())
class heapnode():
    def __init__(self, x, arrnum, index):
        self.x = x
        self.arrnum = arrnum
        self.index = index
        return (self.x, self.arrnum, self.index)

class largestheap():
    def __init__(self, k):
        self.k = k
        self.arr =[]
    def insertheap(self, n):
        if len(self.arr)>self.k:


arr= []
for i in range(t):
    arr.append(list(map(int, input().split())))

