n = int(input())
arr = list(map(int, input().split()))
def oddtimenum(arr):
    a,b = 0,0
    index = find_index(arr)
    for num in arr:
        if isbit(num, index):
            a ^= num
        else:
            b ^= num
    if a<b:
        return a,b
    else:
        return b,a
def find_index(arr):
    temp = 0
    for num in arr:
        temp ^= num
    index = 0
    while temp != 1:
        temp = temp >> 1
        index += 1
        
    return index
def isbit(num, index):
    return (num>>index)&1
a,b = oddtimenum(arr)
print(a,b)