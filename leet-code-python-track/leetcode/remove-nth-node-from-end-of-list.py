# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        if head.next == None:
            return 

        temp = head
        c = 0
        while temp.next:
            c +=1
            temp = temp.next

        temp1 = head
        temp2 = head.next
        if c - n == -1:
            head = temp2
            return head
        k = 0
        while temp2.next:
            if k != c-n: 
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                break
            k +=1
        temp1.next = temp2.next
        return head 