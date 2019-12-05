n = int(input())
arr  = map(int, input().split())
def oddtimenum(arr):
    res = 0
    for num in arr:
        res ^= num
    return res
print(oddtimenum(arr))
