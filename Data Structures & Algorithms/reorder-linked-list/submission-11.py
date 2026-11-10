# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        #1 - 2 - 3 - 4 - 5 - 6
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = prev = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        first = head
        second = prev

        while second:
            l1 = first.next
            l2 = second.next
            first.next = second
            second.next = l1
            first, second = l1,l2
        