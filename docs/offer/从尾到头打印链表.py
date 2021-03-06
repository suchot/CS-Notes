# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    #递归法
    def printListFromTailToHead1(self, listNode):
        res = []
        if listNode:
            res.extend(self.printListFromTailToHead1(listNode.next))
            res.append(listNode.val)
        return res
# 头节点法
    def printListFromTailToHead2(self, listNode):
        if not listNode:
            return []
        dummy = ListNode(-1)
        while listNode:
            temp = listNode.next
            listNode.next = dummy.next
            dummy.next = listNode
            listNode = temp

        res = []
        dummy = dummy.next
        while dummy:
            res.append(dummy.val)
            dummy = dummy.next
        return res
            
            

# 栈法
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
    print(S.printListFromTailToHead2(dummy))
