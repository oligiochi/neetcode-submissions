
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head

        # 1. Interweaving
        while curr:
            new = Node(curr.val, curr.next, None)
            curr.next = new
            curr = new.next

        # 2. Random pointers
        curr = head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. Separation
        curr = head
        newhead = head.next
        prec = newhead

        while curr:
            curr.next = prec.next

            if prec.next:
                prec.next = prec.next.next

            curr = curr.next
            prec = prec.next

        return newhead
