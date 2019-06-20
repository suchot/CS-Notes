# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar1(self, s):
        # write code here
        if not s:
            return -1
        dict_s = {}
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        for i in range(len(s)):
            if dict_s[s[i]]==1:
                return i
        return -1
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        dict_s = [0 for i in range(256)]
        for i in s:
            dict_s[ord(i)] += 1
        for i in range(len(s)):
            if dict_s[ord(s[i])]==1:
                return i
        return -1