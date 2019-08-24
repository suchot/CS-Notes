class Solution():
    def connect(self,arr):
        j_num = arr[0]
        arr =arr[1::]
        arr.sort()
        if len(arr)<=3:
            return min(arr)
        res  = 0
        index = 0
        while arr[-3] != 0:
            res += arr[index]
            if index + 3>=j_num:
                arr[-3]=0
            else:
                for i in range(3,-1, -1):
                    temp = arr[index]
                    arr[index+i]-= temp
            index+=1
        return res

if __name__ == "__main__":
    S = Solution()
    c = int(input())
    con =[]
    for i in range(c):
        #l = list(map(int, input().split()))
        l = [4,2,3,3,99]
        print(S.connect(l))
    