# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev
        return prev
        