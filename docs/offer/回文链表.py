# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack = []
        if not head and not head.next:
            return False
        slow, fast = head, head.next
        
        while fast:
            stack.append(slow)
            slow = head.next
            fast = fast.next.next
        mid = slow
        stack