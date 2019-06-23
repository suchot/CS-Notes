# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = head
        if not head or not head.next:
            return head
        len_k = 1
        while head.next:
            len_k += 1
            head = head.next
        head.next = first
        cut_point = (len_k - k%len_k)
        for i in range(cut_point):
            head = head.next
            
        result = head.next
        head.next = None
        return result
            
        
