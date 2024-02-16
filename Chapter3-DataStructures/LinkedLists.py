class SingleNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class DoublyNode:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

single_root = SingleNode(1)
single_root.next = SingleNode(2)
single_root.next.next = SingleNode(3)

doubly_linked_list = DoublyNode(1)
doubly_linked_list.next = DoublyNode(2)
doubly_linked_list.next.prev = doubly_linked_list
doubly_linked_list.next.next = DoublyNode(3)
doubly_linked_list.next.next.prev = doubly_linked_list.next
