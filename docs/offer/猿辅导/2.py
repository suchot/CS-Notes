class Solution():
    def baoshu(self,l , m):
        lenl = len(l)
        d_l = {}
        for i in range(lenl):
            d_l[l[i]]=d_l.get(l[i],0)+1
        res = []
        for i in range(lenl):
            if d_l[l[i]]>m:
                continue
            res.append(str(l[i]))
        return res

if __name__ == "__main__":
    S = Solution()
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    res = S.baoshu(l,m)
    print(' '.join(res))