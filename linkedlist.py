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

    def delete_node(self, data):
        # return if empty list
        if self.head is None:
            return
        # Store head node
        temporary_node = self.head

        # If head node itself holds the data to be deleted, update the list head, which removes the node.
        if temporary_node is not None:
            if temporary_node.data == data:
                self.head = temporary_node.next
                return

        # Search for the data to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temporary_node is not None:
            if temporary_node.data == data:
                break
            previous_node = temporary_node
            temporary_node = temporary_node.next

        # If the data was not present in the list, simply return
        if temporary_node is None:
            return

        # unlink the previous node, and link to the next node
        previous_node.next = temporary_node.next

    def print_list(self):
        temporary_data = self.head
        print('\n=== Linked List Elements===')
        while temporary_data:
            print(f'List element: {temporary_data.data}'),
            temporary_data = temporary_data.next

    def insert_node(self, previous_node_data, data):
        temporary_node = self.head

        while temporary_node is not None:
            if temporary_node.data == previous_node_data:
                break
            temporary_node = temporary_node.next

        node = Node(data)  # Add node
        node.next = temporary_node.next
        temporary_node.next = node
