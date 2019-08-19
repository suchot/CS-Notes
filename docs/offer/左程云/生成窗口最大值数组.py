lens, w = map(int, input().split())
l =  list(map(int,input().split()))
queue = []
res = []
if lens<w or w<1:
    print(res)
start, end = 0, lens
while start<end:
    if queue and start-queue[0]>=w:
        queue.pop(0)
    while queue and l[queue[-1]]<l[start]:
        queue.pop()
    queue.append(start)
    if start>=w-1:
        res.append(l[queue[0]])
    start+=1
print(' '.join(map(str, res)))
