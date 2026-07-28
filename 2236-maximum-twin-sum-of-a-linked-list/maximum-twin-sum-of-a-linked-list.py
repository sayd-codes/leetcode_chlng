# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
      
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        i = 0
        j = len(arr) - 1
        ans = 0

        while i < j:
            ans = max(ans, arr[i] + arr[j])
            i += 1
            j -= 1

        return ans
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        