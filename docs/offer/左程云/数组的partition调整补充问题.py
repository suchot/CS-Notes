N = int(input())
arr =list(map(int, input().split()))
def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def colorsort(arr):
    if len(arr)<=1:
        return arr
    left = -1
    index = 0
    right = len(arr)
    while index <right:
        if arr[index]==0:
            left +=1
            swap(arr, left, index)
        elif arr[index]==2:
            right -= 1
            swap(arr, index, right)
            continue
        index += 1
colorsort(arr)
print(' '. join(map(str, arr)))