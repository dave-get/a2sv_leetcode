# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        node = head
        temp = node.next
        while temp:
            if node.val == temp.val:
                temp = temp.next
                node.next = None
                node.next = temp
            else:
                node = temp
                temp = node.next
        return head