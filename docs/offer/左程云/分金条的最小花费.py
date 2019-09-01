import heapq
n = int(input())
minheap = list(map(int, input().split()))
if not minheap:
    print(0)
res = 0
heapq.heapify(minheap)
while minheap:
    try:
        k = heapq.heappop(minheap)+heapq.heappop(minheap)
        res += k
        heapq.heappush(minheap, k)
    except:
        break
print(res)
