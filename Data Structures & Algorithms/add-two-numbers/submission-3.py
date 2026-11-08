# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=l1
        b=l2
        out=None
        i=5
        while a and b:
            if (not a.next) and b.next:
                a.next=ListNode(0,None)
            elif (not b.next) and a.next:
                b.next=ListNode(0,None)
            a=a.next
            b=b.next
        a=l1
        b=out=l2

        while a and b:
            s=a.val+b.val
            r=0
            i-=1
            if s>=10:
                s=s-10
                r=1
            b.val=s
            if i==0:
                print(s)
            
            if b.next:
                b.next.val+=r
            elif r>=1:
                print(r)
                b.next=ListNode(r,None)
            
            b=b.next
            a=a.next
        return out