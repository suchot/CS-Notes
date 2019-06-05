# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # 不能用self.in 命名　会报错。　莫名奇妙
        self.in1 = []
        self.out = []
    def push(self, node):
        # write code here
        self.in1.append(node)
    def pop(self):
        # return xx
        if self.out==[]:
            while self.in1:
                self.out.append(self.in1.pop())
            return self.out.pop()
        return self.out.pop()