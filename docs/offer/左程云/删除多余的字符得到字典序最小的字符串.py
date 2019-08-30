class Solution():
    def removedupletter(self,n,m, s1, s2):
        if n!=m:
            return False
        dict_s = {}
        for s in s1:
            dict_s[s]=dict_s.get(s,0) + 1
        for s in s2:
            dict_s[s]=dict_s.get(s,0)-1
            if dict_s[s]<0:
                return False
        return True
if __name__ == "__main__":
    S = Solution()
    s1 = input()
    print(S.removedupletter(n,m, s1,s2))