from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node

    def add_to_beginning(self, data):
        node = Node(data)  # Add node
        node.next = self.head  # Update current node with the current (old) head
        self.head = node  # Now update starting point in list

    def contains(self, data):
        status = False

        temporary_node = self.head
        while temporary_node is not None:
            if temporary_node.data == data:
                status = True
            temporary_node = temporary_node.next

        return status
