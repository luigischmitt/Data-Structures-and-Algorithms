# Creating a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining a class to linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Append at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)

    # Insert a new node after a prev node
    def insert_after(self, prev_node, data):
        if not prev_node:
            print("O nó anterior deve estar na lista.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        
        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return

        prev = None
        while current is not None:
            if current.data == key:
                break
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

# Example of usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()  # 1 -> 2 -> 3 -> None

linked_list.insert_after(linked_list.head, 4)
linked_list.print_list()  # 1 -> 4 -> 2 -> 3 -> None

linked_list.delete_node(2)
linked_list.print_list()  # 1 -> 4 -> 3 -> None
