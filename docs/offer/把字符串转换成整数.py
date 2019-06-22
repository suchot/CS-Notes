# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        isnegitive = False
        if s[0] == '-':
            isnegitive = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = 0
        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                num = ord(s[i]) - ord('0')
                res = res *10 + num
            else:
                return 0
        if isnegitive:
            res = -res
        return res
