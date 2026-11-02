# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        test=head
        prec=None
        i=0
        while test and i < n:
            test=test.next
            i+=1
        print(bool((not test) or i<n))
        if (not test) or i<n:
            if current.next:
                moment=current.next
                del current
                return moment            
        else:
            while test:
                prec=current
                current=current.next
                test=test.next
            print(current.val,prec.val)
            prec.next=current.next
            del current
            return head
        