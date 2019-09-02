n, p = map(int, input().split())
arr= list(map(int, input().split()))
def acprodcuct(arr):
    if len(arr)<=1:
        return arr
    C = [1 for i in range(len(arr))]
    for i in range(1, len(arr)):
        C[i] = C[i-1]*arr[i-1]
    temp = 1
    for j in range(len(arr)-2, -1, -1):
        temp *= arr[j+1]
        C[j] = temp*C[j]
    return C
res = acprodcuct(arr)
res = list(map(lambda x: x%p, res))
print(' '.join(map(str, res)))
# 内存超限