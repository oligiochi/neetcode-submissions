class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        prev = None
        curr = head

        alf = self.size(curr) // 2

        # Trovo il punto di separazione
        for _ in range(alf):
            curr = curr.next

        # Inverto la seconda metà
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        reverse = prev
        curr = head

        # Merge delle due metà
        for _ in range(alf):
            next_node = curr.next
            next_reverse = reverse.next

            curr.next = reverse
            reverse.next = next_node

            curr = next_node
            reverse = next_reverse

        # Importante: termina la lista
        curr.next = None

    def size(self, head: Optional[ListNode]) -> int:
        curr = head
        c = 0

        while curr:
            c += 1
            curr = curr.next

        return c