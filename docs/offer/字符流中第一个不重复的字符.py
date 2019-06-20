# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.chr = [-1 for i in range(256)]
        self.index = 0
    def FirstAppearingOnce(self):
        # write code here
        min_index = float('inf')
        ch = '#'
        for i in range(256):
            if self.chr[i] < min_index and self.chr[i]>=0:
                min_index = self.chr[i]
                ch = chr(i)
        return ch
    def Insert(self, char):
        # write code here
        if (self.chr[ord(char)] >=0 ):
            self.chr[ord(char)] = -2
        if (self.chr[ord(char)] == -1):
            self.chr[ord(char)] = self.index
        self.index += 1
