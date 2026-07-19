# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = None
        node = head

        while node:
            nxt = node.next
            node.next = dummy
            dummy = node 
            node = nxt
        
        return dummy