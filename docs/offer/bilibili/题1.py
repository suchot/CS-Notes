class Solution():
    def numdecodings(self, s):
        pp, p =1, int(s[0] !='0')
        for i in range(1, len(s)):
            pp, p = p, pp*(9<int(s[i-1:i+1])<=26) +p*(int(s[i])>0)
        return p
if __name__ == "__main__":
    S = Solution()
    ls = input()
    print(S.numdecodings(ls))