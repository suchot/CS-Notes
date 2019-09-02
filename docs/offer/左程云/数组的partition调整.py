N= input()
arr =list(map(int, input().split()))
def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j]=temp
def leftunique(arr):
    if len(arr)<=1:
        return arr
    left, right =0, 1
    while right !=len(arr):
        if arr[right] !=arr[left]:
            left += 1
            swap(arr, left, right)
        right+=1
leftunique(arr)
print(' '.join(map(str,arr)))