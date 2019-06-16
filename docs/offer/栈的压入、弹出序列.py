# -*- coding:utf-8 -*-
# 原理：如果下一个弹出的数字刚好是栈顶数字，那么直接弹出；如果下一个弹出的数字不在栈顶，则把压栈序列中还没有入栈的数字压入辅助栈，直到把下一个需要弹出的数字压入栈顶为止，如果所有数字都压入栈后仍然没有找到下一个弹出的数字，那么该序列不可能是一个弹出序列。
class Solution:
    def __init__(self):
        self.stack = []
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV and not popV:
            return False
        while pushV:
            self.stack.append(pushV.pop(0))
            while self.stack and self.stack[-1]==popV[0]:
                self.stack.pop()
                popV.pop(0)
        return not self.stack 

