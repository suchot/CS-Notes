n = int(input())
arr = list(map(int, input().split()))
def maxsum(arr):
    if not arr:
        return 0
    maxvalue = arr[0]
    cur = arr[0]
    for i in range(1, len(arr)):
        cur += arr[i]
        maxvalue = max(cur, maxvalue)
        cur = 0 if cur<0 else cur
    return maxvalue 
print(maxsum(arr))