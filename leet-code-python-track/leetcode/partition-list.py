# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode()
        head2 = ListNode()

        current = head
        g = head1
        l = head2
        while current:
            if current.val >= x:
                g.next = current
                g = g.next
            else:
                l.next = current
                l = l.next
            current = current.next
        l.next = head1.next
        g.next = None
        return head2.next

        