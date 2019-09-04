import heapq
t, k = map(int, input())
import heapq
heap = []
T, K = map(int, input().split())
for i in range(T):
    add = list(map(int, input().split()))
    for j in range(add[0]):
        heapq.heappush(heap, add[j + 1])
res = heapq.nlargest(K, heap)
for k in range(K):
    print(res[k], end=" ")

