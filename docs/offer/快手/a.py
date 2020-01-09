# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s.reverse()
        return ' '.join(s)
if __name__ == "__main__":
    S=Solution()
    s = input().split()
    s = ' '.join(s)
    if s[-1]=='.':
        isdot = True
        s =s[:-1]
    s = list(s.split())
    res = S.ReverseSentence(s)
    if isdot:
        print(res+'.')
    else:
        print(res)