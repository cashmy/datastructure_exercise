class BinaryNode:

    def __init__(self, data):
        self.right_child_node = None
        self.left_child_node = None
        self.data = data

    def insert_node(self, data):
        if self.data:
            if data < self.data:  # Smaller nodes to the left, larger to the right
                if self.left_child_node is None:
                    self.left_child_node = BinaryNode(data)
                else:
                    self.left_child_node.insert_node(data)  # Move down the tree
            elif data > self.data:
                if self.right_child_node is None:
                    self.right_child_node = BinaryNode(data)
                else:
                    self.right_child_node.insert_node(data)  # move down the tree
        else:  # This is the parent node
            self.data = data

    def search_tree(self, data):
        if self.data == data:
            self.search_results(data, self.data)
        else:
            if data < self.data:
                if self.left_child_node:
                    self.left_child_node.search_tree(data)
                else:
                    self.search_results(data, None)
            elif data > self.data:
                if self.right_child_node:
                    self.right_child_node.search_tree(data)
                else:
                    self.search_results(data, None)

    def print_tree(self):
        # This prints a "sorted" tree.
        # Because the current "rule" is that left is the smaller side and right is the larger side

        # Print left side
        if self.left_child_node:  # if exists move down the branch 'smaller number'
            self.left_child_node.print_tree()

        print(self.data),  # print self

        # Print right side
        if self.right_child_node:  # Next check for the right side 'larger number'
            self.right_child_node.print_tree()

    @staticmethod
    def search_results(data, found_data):
        print(f'Node to search for: {data}')
        if found_data:
            print(f'Node found: {found_data}')
        else:
            print(f'Node: {data} not found')
