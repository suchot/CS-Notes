version1, version2 = input().split(' ')
v1 = list(map(int, version1.split('.')))
v2 = list(map(int, version2.split('.')))

if v1<v2:
    print(-1)
elif v1>v2:
    print(1)
else:
    print(0)