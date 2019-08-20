class Solution():
    def conv(self, pic, kernel, h, m, w):
        res =[]
        if not pic:
            return res
        res = [[0 for i in range(w-m+1)] for j in range(h-m+1)]
        for i in range(h-m+1):
            for j in range(w-m+1):
                temp = 0 
                for u in range(m):
                    for v in range(m):
                        temp += pic[i+u][j+v]*kernel[u][v]
                res[i][j]=min(int(temp), 255)
        return res

if __name__ == "__main__":
    h,w = map(int, input().split())
    pic = []
    for i in range(h):
        w_col = list(map(int,input().split()))
        pic.append(w_col)
    m = int(input())
    kernel =[]
    for j in range(m):
        k_col = list(map(float,input().split()))
        kernel.append(k_col)
    S = Solution()
    res = S.conv(pic, kernel,h,m,w)
    rows = len(res)
    for i in range(rows):
        s = res[i]
        res_s =' '.join(map(str, s))
        print(res_s)

