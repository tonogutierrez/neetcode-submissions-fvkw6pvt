"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dicc = {None:None}
        curr = head

        while curr:
            node = Node(curr.val)
            dicc[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            copy = dicc[curr]
            copy.next = dicc[curr.next]
            copy.random = dicc[curr.random]
            curr = curr.next

        return dicc[head]