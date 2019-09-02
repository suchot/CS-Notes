from itertools import combinations
class Solution():
    def huajiang(self, a, b, k):
        res = 0
        for i in range(a, b+1):
            for red in range(i+1):
                for white in range(i+1):
                    if i==red+white*k:
                        l = ['r' for i in range(red)]
                        l.extend(['w' for j in range(white)])
                        res += len(list(combinations(l,i)))
                    
        return res
if __name__ == "__main__":

    t,k = map(int, input().split())
    for i in range(t):
        a, b = map(int, input().split())
        S = Solution()
        print(S.huajiang(a,b,k))