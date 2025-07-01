class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_from_front(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        else:
            self.tail = new_node # Caso não tenha head, o primeiro elemento é tanto head quanto tail
        self.head = new_node

    def add_from_final(self, value):
        new_node = Node(value)
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None # Precisa disso porque se a lista tivesse apenas 1 nó, após removê-lo a tail estaria apontando para esse nó fantasma ainda
        return removed_value

    def remove_from_final(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return removed_value
    