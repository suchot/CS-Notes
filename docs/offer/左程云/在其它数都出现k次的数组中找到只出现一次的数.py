class Solution():
    def __init__(self, k):
        self.k = k
        self.res = [0]*32
    def oncenum(self,arr):
        once_num = [0]*32
        for num in arr:
            once_num = self.get_ksystem_num(num)
            self.res = self.list_add(self.res, once_num, self.k)
        result = self.ksystem_num2_num(self.res)
        return result
    def list_add(self,a, b, k):
        c = [0]*32
        for i in range(32):
            c[i] = (a[i]+b[i])%k
        return c
    def get_ksystem_num(self, num):
        temp = [0]*32
        index = 0
        while num != 0:
            temp[index] = num%self.k
            num = num//self.k
            index += 1
        return temp

    def ksystem_num2_num(self, num):
        result = 0
        for i in range(31, -1 , -1):
            result = result*self.k+num[i]
        return result
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int,input().split()))
    S = Solution(k)
    print(S.oncenum(arr))