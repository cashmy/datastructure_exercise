class BstAvl:
    # Binary Search Tree - AVL (Adelson-Velsky and Landis)

    def __init__(self, data):
        # Note: if "data" is an object, then this class could be refactored to break out a 'key' value from the
        #       rest of the object and use it appropriately
        self.data = data
        self.left_child_node = None
        self.right_child_node = None
        self.height = 1


class BstTree:
    def insert_node(self, node, data):
        # Parameters: Node = object, data = data value, object, or class

        # Perform normal insert operations
        if not node:  # assume root node
            return BstAvl(data)
        elif data < node.data:
            node.left_child_node = self.insert_node(node.left_child_node, data)
        else:
            node.right_child_node = self.insert_node(node.right_child_node, data)
        # Now update the height of the ancestor node
        node.height = 1 + max(self.get_height(node.right_child_node), self.get_height(node.left_child_node))

        # Now determine the balance factor
        balance = self.get_balance(node)
        return node

    def left_rotate(self, node):
        pass

    def right_rotate(self, node):
        pass

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left_child_node) - self.get_height(node.right_child_node)

    def print_tree_pre_order(self, node):
        if not node:
            return
        print("{0} ".format(node.data), end="")
        self.print_tree_pre_order(node.left_child_node)
        self.print_tree_pre_order(node.right_child_node)
