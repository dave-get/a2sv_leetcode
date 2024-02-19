# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lis = []
        current = head
        if not head:
            return 
        else:
            while current.next:
                lis.append(current.val)
                current = current.next
        lis.append(current.val)
        print(lis)
        if lis == lis[::-1]:
            return True
        return False