# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next  # Salva il prossimo nodo
            curr.next = prev       # Inverte il puntatore
            prev = curr            # Sposta "prev" al nodo corrente
            curr = next_node       # Avanza "curr" al prossimo nodo
            
        return prev  # "prev" sarà la nuova testa della lista