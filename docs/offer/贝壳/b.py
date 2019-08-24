import math
class Solution():
    def maxoil(self, stations, k):
        step = 0
        left, right = 0, 10**9
        while left<right:
            mid = left +((right-left)>>1)
            if self.valid(mid, stations, k):
                right = mid-step
            else:
                left = mid+step
        return mid
    def valid(self, gas, station, k):
        for x in range(len(station)-1):
            dist = station[x+1]-station[x]
            k = -int(dist//gas)-1
        return k>=0



if __name__ == "__main__":
    
    n,m = map(int,input().split())
    a = list(map(int, input().split()))
    S = Solution()
    print(S.maxoil(a,m))