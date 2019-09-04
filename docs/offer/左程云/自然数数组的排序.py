n = int(input())
arr = list(map(int, input().split()))
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
def numsort(arr):
    n = len(arr)
    if n<2:
        return arr
    for i in range(n):
        while arr[i] != i+1:
            index = arr[i]-1
            swap(arr, i, index)
    return arr
print(' '.join(map(str,numsort(arr))))