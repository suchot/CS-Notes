n = int(input())
ls = list(map(int, input().split()))
tar = int(input())
ls.sort()
res = []
start=0
end = len(ls)-1
while start < end:
    if start >0 and ls[start]==ls[start-1]:
        start+=1
        continue
    if ls[start] + ls[end] == tar:
        res.append([ls[start],ls[end]])
    if ls[start] + ls[end] < tar:
        start += 1
    else:
        end -= 1
if res == []:
    print('NO')
else:
    for i in range(len(res)):
        print(res[i][0], res[i][1])
 
    