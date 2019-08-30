# import sys
 # 投机解法
# n,m = sys.stdin.readline().strip().split(" ")
# l1 = sys.stdin.readline().strip()
# l2 = sys.stdin.readline().strip()
 
# if n != m:
#     print("NO")
# elif l1 in (l2 +l2):
#     print("YES")
# else:
#     print("NO")


class Solution():
    def isrotate(self,n,m, s1, s2):
        if not s1 or not s2 or n != m:
            return 'No'
        s = s1+s2
        return self.getindex(s,s1) != -1

    def getindex(self, string, substring):
        '''
        KMP字符串匹配的主函数
        若存在字串返回字串在字符串中开始的位置下标，或者返回-1
        '''
        pnext = self.gen_pnext(substring)
        n = len(string)
        m = len(substring)
        i, j = 0, 0
        while (i<n) and (j<m):
            if (string[i]==substring[j]):
                i += 1
                j += 1
            else:
                j = pnext[j]
                if j == -1:
                    i+=1
                    j+=1
        if (j == m):
            return i-j
        else:
            return -1
                
        
    def gen_pnext(self,substring):
        """
        构造临时数组pnext
        """
        index, m = 0, len(substring)
        pnext = [0]*m
        i = 1
        while i < m:
            if (substring[i] == substring[index]):
                pnext[i] = index + 1
                index += 1
                i += 1
            elif (index != 0):
                index = pnext[index-1]
            else:
                pnext[i] = 0
                i += 1
        for i in range(m-1, 0,- 1):
            pnext[i]=pnext[i-1]
        pnext[0]=-1
        return pnext

if __name__ == "__main__":
    S = Solution()
    n,m = map(int, input().split())
    s1 = input()
    s2 = input()
    print(S.isrotate(n,m, s1,s2))