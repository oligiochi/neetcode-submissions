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
        curr=head
        newhead=Node(0,None,None)
        prec=newhead
        while curr:
            new=Node(curr.val,curr.next,curr)
            prec.next=new
            point=curr.next
            curr.next=new
            curr=point
            prec=new
            
        curr=newhead.next
        while curr:
            corrispotive=curr.random
            if corrispotive.random:
                curr.random=corrispotive.random.next
            else:
                curr.random=None
            curr=curr.next
        return newhead.next
            
        