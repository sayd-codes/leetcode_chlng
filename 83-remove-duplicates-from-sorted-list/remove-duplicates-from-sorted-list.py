# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
       
        nodeA = head

        while nodeA != None:
            nodeB = nodeA.next

            while nodeB != None and nodeA.val == nodeB.val:
                nodeB = nodeB.next

            nodeA.next = nodeB
            nodeA = nodeB

        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        