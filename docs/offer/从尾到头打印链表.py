# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead1(self, listNode):
        res = []
        if listNode:
            res.extend(self.printListFromTailToHead1(listNode.next))
            res.append(listNode.val)
        return res


    def printListFromTailToHead3(self, listNode):
        # write code here
        l = []
        if not listNode:
            return []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        res = []
        while l:
            res.append(l.pop())
        return res
        
if __name__ == "__main__":
    S= Solution()
    dummy = ListNode(1)
    dummy.next = ListNode(2)
    dummy.next.next = ListNode(3)
    print(S.printListFromTailToHead1(dummy))