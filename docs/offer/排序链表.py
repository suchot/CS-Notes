# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        mid_point = slow.next
        slow.next = None
        lnode = self.sortList(head)
        rnode = self.sortList(mid_point)
        return self.merge(lnode, rnode)

    def merge(self, l1, l2):
        res = ListNode(None)
        cur = res
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if not l1:
            cur.next = l2
        if not l2:
            cur.next = l1
        
        return res.next
