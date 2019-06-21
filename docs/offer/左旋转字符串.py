# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)<=1:
            return s
        s1 = s[0:n]
        s2 = s[n:]
        s = self.s_reverse(s1)+ self.s_reverse(s2)
        s = self.s_reverse(s)
        return s
    def s_reverse(self, s):
        s = list(s)
        begin, end = 0, len(s)-1
        while begin<end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1
        return ''.join(s)

#第二种 python的解法
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s)<=1:
            return s
        s1 = s[0:n]
        s2 = s[n:]
        s = s1[::-1]+ s2[::-1]
        s = s[::-1]
        return s

