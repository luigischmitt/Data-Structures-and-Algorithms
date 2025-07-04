class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reversedList(self, head: Node):
        new_list = None

        while head:
            next_node = head.next
            head.next = new_list
            new_list = head
            head = next_node

        return new_list

