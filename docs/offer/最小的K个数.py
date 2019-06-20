import heapq
class TopKheap(object):
    def __init__(self, k):
        self.heap = []
        self.k = k
    def TopKheappush(self, nums):
        # 系统自带的是小顶堆，转负号变大顶堆
        n = -nums
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, n)
        else:
            heapq.heappushpop(self.heap, n)
    def getminK(self):
        res = []
        k = self.k
        while k > 0:
            res.insert(0, -heapq.heappop(self.heap))
            k -= 1
        return res
class Solution:
    # 通过大顶堆来得到最小的几个数
    def GetLeastNumbers_Solution2(self, tinput, k):
        # write code here
        if k > len(tinput) or k<=0:
            return []
        topK = TopKheap(k)
        for i in tinput:
            topK.TopKheappush(i)
        res = topK.getminK()
        return res

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k<=0:
            return []
        start, end = 0, len(tinput)-1
        index = self.partition(tinput, start, end)
        while index != (k-1):
            if index >k-1:
                end = index -1
                index = self.partition(tinput, start, end)
            else:
                start = index + 1
                index = self.partition(tinput, start, end)
        res = tinput[0:k]
        return res
    # 看算法导论
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
    tinput, k = [3,4,7,1,4,10,9], 3
    
    tinput, k = [3,2,1,5,6,4], 3
    S = Solution()
    print(S.findKthLargest(tinput, k))