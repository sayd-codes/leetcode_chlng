# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
       
        first = head

        for _ in range(k - 1):
            first = first.next

        fast = head

        for _ in range(k):
            fast = fast.next

        second = head

        while fast:
            fast = fast.next
            second = second.next

        
        first.val, second.val = second.val, first.val

        return head
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        